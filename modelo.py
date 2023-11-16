import sqlite3

class BaseDeDatos():
    def __init__(self) -> None:
        self.conexion = sqlite3.connect("base.db")
        self.cursor = self.conexion.cursor()
        
        ###CREO LAS TABLAS NECESARIAS:
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Facturacion (id INTEGER, Fecha TEXT, Concepto TEXT, Monto NUMERIC, PRIMARY KEY(id AUTOINCREMENT))")
        self.conexion.commit()

    def cargar_datos(self,fecha,concepto,monto):
        
        sql_carga = "INSERT INTO facturacion VALUES (null,?,?,?)"
        datos=(fecha,concepto,monto)
        self.cursor.execute(sql_carga,datos)
        self.conexion.commit()
    
    def borrar_datos(self,borrar):
         
        sql = "DELETE FROM facturacion WHERE id = ?;" 
        borrar_datos = borrar
        self.cursor.execute(sql,borrar_datos) 

         
    def actualizar_treeview(self):
        sql_treeview = "SELECT* FROM facturacion ORDER BY Fecha ASC"
        self.cursor.execute(sql_treeview)
        datos = self.cursor.fetchall()
        return datos

class MiBaseDeDatos():
    def __init__(self, nombre_base_de_datos = "facturacion.db"):
        """Creacion de la base datos y sus conexiones 

        Args:
            nombre_base_de_datos (str, optional): _description_. Defaults to "facturacion.db".
        """        
        self.nombre_base_de_datos = nombre_base_de_datos
        self.conexion = sqlite3.connect(self.nombre_base_de_datos)
        self.cursor = None
        self.conectar()
        self.crear_tablas()

    def conectar(self):
        try:
            self.conexion.isolation_level = None  # Desactiva el autocommit
            self.cursor = self.conexion.cursor()
            print("---> Conexión abierta")
        except sqlite3.Error as error:
            print(f"Error al conectar a la base de datos: {error}")

    def crear_tablas(self):
        if self.cursor:
            try:
                #CREO TABLA - FACTURACION
                self.cursor.execute("""CREATE TABLE IF NOT EXISTS facturacion (
                                    fac_int_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    fac_date_fecha DATE,
                                    fac_int_idconcepto INTEGER,
                                    fac_bol_monto REAL,
                                    fac_txt_cuilcliente TEXT
                                    )
                                    """)
                #CREO TABLA  -  CONCEPTOS
                self.cursor.execute("""CREATE TABLE IF NOT EXISTS conceptos (
                                    con_int_idconcepto INTEGER PRIMARY KEY AUTOINCREMENT,
                                    con_txt_descripcion TEXT,
                                    con_txt_estado  TEXT
                                    )
                                    """)
                #CREO TABLA  -  CATEGORIA_MONOTRIBUTO
                self.cursor.execute("""CREATE TABLE IF NOT EXISTS categoria_monotributo(
                                    cat_int_idcategoria INTEGER PRIMARY KEY AUTOINCREMENT,
                                    cat_txt_descripcion TEXT,
                                    cat_bol_montotope REAL,
                                    cat_txt_estado TEXT
                                    )
                                    """)
                #CREO TABLA  -  CONFIG_APP
                self.cursor.execute("""CREATE TABLE IF NOT EXISTS config_app(
                                    config_int_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    config_txt_tipo TEXT,
                                    config_txt_valor TEXT
                                    )
                                    """)
                self.conexion.commit()
                print("---> Bases validadas/creadas")
            except sqlite3.Error as error:
                print(f"Error en la actualización de datos: {error}")
                self.conexion.rollback()

    def desconectar(self):
        if self.conexion:
            self.conexion.close()
            print("---> Conexión cerrada")

    def carga_datos_iniciales(self):
        """ingresa los datos iniciales de categoria de monotributo, configuracion inicial.
        """        
        if self.cursor:
            try:
                sql = """
                    INSERT OR IGNORE INTO categoria_monotributo (cat_txt_descripcion, cat_bol_montotope, cat_txt_estado)
                    SELECT ?, ?, ?
                    WHERE NOT EXISTS (SELECT 1 FROM categoria_monotributo WHERE cat_txt_descripcion = ?)
                """
                data = ('A',1414762.58,"activo",'A')
                self.cursor.execute(sql, data)

                data = ('B',2103025.45,"activo",'B')
                self.cursor.execute(sql, data)

                data = ('C',2944235.6,"activo",'C')
                self.cursor.execute(sql, data)

                data = ('D',3656604.33,"activo",'D')
                self.cursor.execute(sql, data)

                data = ('E',4305799.15,"activo",'E')
                self.cursor.execute(sql, data)

                data = ('F',5382248.94,"activo",'F')
                self.cursor.execute(sql, data)

                data = ('G',6458698.71,"activo",'G')
                self.cursor.execute(sql, data)

                data = ('H',7996484.12,"activo",'H')
                self.cursor.execute(sql, data)

                #ACA ESTOY CARGANDO EN UNA BASE config el tipo color_fondo y el valor #004080
                sql = """
                INSERT INTO config_app (config_txt_tipo , config_txt_valor) 
                SELECT ?,?
                WHERE NOT EXISTS (SELECT 1 FROM config_app WHERE config_txt_tipo = 'color_fondo')
                """
                data = ('color_fondo','#004080')
                self.cursor.execute(sql, data)

                #ACA ESTOY CARGANDO EN UNA BASE config el tipo 'link_afip' y el valor 'https://www.afip.gob.ar/monotributo/categorias.asp'
                sql = """
                INSERT INTO config_app (config_txt_tipo , config_txt_valor) 
                SELECT ?,?
                WHERE NOT EXISTS (SELECT 1 FROM config_app WHERE config_txt_tipo = 'link_afip')
                """
                data = ('link_afip','https://www.afip.gob.ar/monotributo/categorias.asp')
                self.cursor.execute(sql, data)


                self.conexion.commit()
                print("datos cargados correctamente")
            except sqlite3.Error as error:
                print(f"Error en la carga inicial: {error}")
                self.conexion.rollback()

    def return_config(self,parametro):
        """CONSULA EN LA BASE DE DATOS, DEPENDIENDO DEL PARAMETRO EN LA TABLA CONFIGURACION

        Args:
            parametro (STR): 'color_fondo','link_afip'

        Returns:
            str: config_txt_valor 
        """            
        if self.cursor:
                        try:
                            sql = """
                                SELECT config_txt_valor 
                                FROM config_app 
                                WHERE config_txt_tipo = ?
                            """
                            data = (parametro,)
                            self.cursor.execute(sql, data)
                            retorno = (self.cursor.fetchall()[0][0])
                            return retorno
                        except sqlite3.Error as error:
                            print(f"Error a retornar {parametro}: {error}")
                            self.conexion.rollback()
                        
    def grabar_config(self,config_txt_tipo, cinfig_txt_valor):
        """GRABA UNA NUEVA CONFIGURACION

        Args:
            config_txt_tipo (STR): 'color_fondo','link_afip'
            cinfig_txt_valor (STR): nuevo_valor
        """            
        if self.cursor:
                    try:
                        sql = """
                            UPDATE config_app
                            SET config_txt_valor = ?
                            WHERE config_txt_tipo = ?
                        """
                        data = (cinfig_txt_valor,config_txt_tipo,)
                        self.cursor.execute(sql, data)
                        print(f"-->configuracion {config_txt_tipo}grabada exitosamente")
                    except sqlite3.Error as error:
                        print(f"Error a retornar {cinfig_txt_valor,config_txt_tipo}: {error}")
                        self.conexion.rollback()

    def trae_conceptos(self):
        #datos =["Ingreso Nuevo","Colegio médico","Hospital","Intecnus","Particular"] 
        #return datos
        if self.cursor:
            try:
                sql = """
                    SELECT *
                    FROM conceptos
                    WHERE con_txt_estado = 'activo'
                    """ 
                self.cursor.execute(sql)
                retorno = (self.cursor.fetchall())
                print(retorno)
                return retorno
            except sqlite3.Error as error:
                print(f"Error a retornar conceptos: {error}")
                self.conexion.rollback()
        
    def agrega_concepto(self,concepto):
        if self.cursor:
            try:
                sql = """
                    INSERT INTO conceptos (con_txt_descripcion , con_txt_estado) 
                    SELECT ?,?
                    WHERE NOT EXISTS (SELECT 1 FROM conceptos WHERE con_txt_descripcion = ?)
                """
                data = [concepto,"activo",concepto]
                self.cursor.execute(sql,data)
            except sqlite3.Error as error:
                        print(f"Error a grabar {concepto}: {error}")
                        self.conexion.rollback()




#    def modificar_factura(self,factura_id, nueva_fecha, nuevo_id_concepto, nuevo_monto, nuevo_cuil_cliente):
#        """MODIFICA UNA FACTURA EXISTENTE EN LA BASE DE DATOS
#
#        Args:
#            factura_id (_int_): _factura a modificar_
#            nueva_fecha (_date_): _nueva fecha_
#            nuevo_id_concepto (_int_): _nuevo id concepto_
#            nuevo_monto (_bol_): _nuevo monto_
#            nuevo_cuil_cliente (_str_): _nuevo cuil de cliente_
#        """        
#        try:
#            self.conectar()
#            sql = "UPDATE facturacion SET fac_date_fecha = ?, fac_int_idconcepto = ?, fac_bol_monto = ?, fac_txt_cuilcliente = ? WHERE fac_int_id = ?"
#            data = (nueva_fecha, nuevo_id_concepto, nuevo_monto, nuevo_cuil_cliente, factura_id)
#            self.cursor.execute(sql,data)
#            self.conexion.commit()
#            print(f"Factura con ID {factura_id} modificada correctamente")
#        except sqlite3.Error as error:
#            print(f"Error al modificar la factura: {error}")
#            self.conexion.rollback()
#        
#    def borrar_factura(self,factura_id):
#        try:
#            self.conectar()
#            sql = "DELETE FROM facturacion WHERE fac_int_id = ?"
#            data = (factura_id,)
#            self.cursor.execute(sql,data)
#            self.conexion.commit()
#            print(f"Factura con ID {factura_id} fue eliminada correctamente ")
#        except sqlite3.Error as error:
#            print(f"Error al eliminar la factura: {error}")
#            self.conexion.rollback()




if __name__ == "__main__":
    # Uso de la clase Factura
    mibase = MiBaseDeDatos()
    print("si le pido a la funcion link_afip, me devuelve:" , mibase.return_config('link_afip'))
    print("si le pido a la funcion color_fondo, me devuelve:" , mibase.return_config('color_fondo'))



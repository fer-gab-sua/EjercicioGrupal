import sqlite3
import re
import datetime



class MiBaseDeDatosConnect():
    def __init__(self, nombre_base_de_datos = "facturacion.db"):
        """Creacion de la base datos y sus conexiones 

        Args:
            nombre_base_de_datos (str, optional): _description_. Defaults to "facturacion.db".
        """        
        self.nombre_base_de_datos = nombre_base_de_datos
        self.conexion = None
        self.cursor = None
        self.crear_tablas()

    def conectar(self):
        try:
            self.conexion = sqlite3.connect(self.nombre_base_de_datos)
            self.conexion.isolation_level = None  # Desactiva el autocommit
            self.cursor = self.conexion.cursor()
            print("-> Conexión abierta")
        except sqlite3.Error as error:
            print(f"Error al conectar a la base de datos: {error}")

    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()
            print("-> Conexión cerrada")
            print("\n")

    def crear_tablas(self):
        self.conectar()
        try:
            #CREO TABLA - FACTURACION
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS facturacion (
                            fac_int_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            fac_date_fecha DATE,
                            fac_txt_concepto TEXT,
                            fac_bol_monto REAL,
                            instante DATETIME DEFAULT CURRENT_TIMESTAMP
                            )
                            """)
            #CREO EL TRIGGER PARA FACTURACION
            self.cursor.execute("""CREATE TRIGGER IF NOT EXISTS actualizar_instante
                            AFTER INSERT ON facturacion
                            FOR EACH ROW
                            BEGIN
                                UPDATE facturacion SET instante = DATETIME('now', 'localtime') WHERE fac_int_id = NEW.fac_int_id;
                            END;
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
                                cat_txt_fecha DATE
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
            print("---> Bases validadas/creadas <---")
        except sqlite3.Error as error:
            print(f"Error en la actualización de datos: {error}")
            self.conexion.rollback()
        finally:
            self.desconectar()

    def carga_datos_iniciales(self):
        """ingresa los datos iniciales de categoria de monotributo, configuracion inicial.
        """  
        self.conectar()
        try:
            sql = """
                INSERT OR IGNORE INTO categoria_monotributo (cat_txt_descripcion, cat_bol_montotope, cat_txt_fecha)
                SELECT ?, ?, ?
                WHERE NOT EXISTS (SELECT 1 FROM categoria_monotributo WHERE cat_txt_descripcion = ?)
            """
            data = ('A',1414762.58,"01/01/2023",'A')
            self.cursor.execute(sql, data)

            data = ('B',2103025.45,"01/01/2023",'B')
            self.cursor.execute(sql, data)

            data = ('C',2944235.6,"01/01/2023",'C')
            self.cursor.execute(sql, data)

            data = ('D',3656604.33,"01/01/2023",'D')
            self.cursor.execute(sql, data)

            data = ('E',4305799.15,"01/01/2023",'E')
            self.cursor.execute(sql, data)

            data = ('F',5382248.94,"01/01/2023",'F')
            self.cursor.execute(sql, data)

            data = ('G',6458698.71,"01/01/2023",'G')
            self.cursor.execute(sql, data)

            data = ('H',7996484.12,"01/01/2023",'H')
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
            print("---> Datos iniciados cargados/validados con exito")
        except sqlite3.Error as error:
            print(f"Error en la carga inicial: {error}")
            self.conexion.rollback()
        finally:
            self.desconectar()

class ModeloCategorias(MiBaseDeDatosConnect):
#metodos de retorno y grabacion de categorias
    def traer_categorias(self):
        self.conectar()
        try:
            sql = """
                SELECT *
                FROM categoria_monotributo
                WHERE cat_txt_fecha = "01/01/2023"
                """ 
            data = ("01/01/2023",)
            self.cursor.execute(sql)
            retorno = (self.cursor.fetchall())
            print("---> Categorias retornados con exito metodo:trae_categorias()")
            return retorno
        except sqlite3.Error as error:
            print(f"Error a retornar categorias: {error}")
            self.conexion.rollback()
        finally:
            self.desconectar()

    def cambiar_categorias(self,bloque):
        self.conectar()
        try:
            for cat in bloque:
                print(cat[0])
                print(cat[1])
                print(cat[2])
                sql = """INSERT OR IGNORE INTO categoria_monotributo (cat_txt_descripcion, cat_bol_montotope, cat_txt_fecha)
                SELECT ?, ?, ?
                """
                #WHERE NOT EXISTS (SELECT 1 FROM categoria_monotributo WHERE cat_txt_estado = "activo")
                #   """
                data = (cat[0],(cat[1]),(cat[2]))
                self.cursor.execute(sql,data)
                print("---> Categorias agregadas con exito metodo:cambiar_categorias()")

        except sqlite3.Error as error:
            print(f"Error a retornar categorias: {error}")
            self.conexion.rollback()
        finally:
            self.desconectar()


class ModeloParaVista(MiBaseDeDatosConnect):
#metodos de retorno para funcionamiento de pantalla
    def actualizar_treeview(self):
        self.conectar()
        try:
            sql_treeview = """SELECT* 
                            FROM facturacion 
                            ORDER BY strftime('%Y-%m-%d', fac_date_fecha) ASC"""
            self.cursor.execute(sql_treeview)
            datos = self.cursor.fetchall()
            print("---> Datos traidos para el treeview generados correctamente metodo:actualizar_treeview")
            print(datos)

            return datos
        except sqlite3.Error as error:
            print(f"Error a cargar_datos: {error}")
            self.conexion.rollback()
        finally:
            self.desconectar()

    def sumar_facturacion(self):
        self.conectar()
        try:
            sql = """SELECT SUM (fac_bol_monto)
                            FROM facturacion 
                            """
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            print("---> Suma generada con exito")
            return datos
        except sqlite3.Error as error:
            print(f"Error en sumar facturas: {error}")
            self.conexion.rollback()
        finally:
            self.desconectar()      

class Crud(MiBaseDeDatosConnect):
###ABM DE FACTURAS
    def cargar_datos(self,fecha,concepto,monto,instante):
        self.conectar()
        try:
            sql_carga = "INSERT INTO facturacion VALUES (null,?,?,?,?)"
            datos=(fecha,concepto,monto,instante)
            self.cursor.execute(sql_carga,datos)
            self.conexion.commit()
            print ("---> Los registros fueron guardados con éxito.")
        except sqlite3.Error as error:
            print(f"Error a cargar_datos: {error}")
            self.conexion.rollback()
        finally:
            self.desconectar()

    def borrar_datos(self,borrar):
        self.conectar()
        try:
            sql = "DELETE FROM facturacion WHERE fac_int_id = ?;" 
            borrar_datos = borrar
            self.cursor.execute(sql,borrar_datos) 
            self.conexion.commit()
            print (f"---> El registro {borrar} se borró con éxito.")
        except sqlite3.Error as error:
            print(f"Error a borrar registro id {borrar}: {error}")
            self.conexion.rollback()
        finally:
            self.desconectar()

    def actualizar_datos(self,fecha,concepto,monto,id):
        self.conectar()
        try:
            sql_update = "UPDATE Facturacion set fac_date_fecha = ?,\
                                                    fac_txt_concepto = ?,\
                                                        fac_bol_monto =? \
                                                        WHERE fac_int_id = ? "
            datos = (fecha,concepto,monto,id)
            self.cursor.execute(sql_update,datos)
            self.conexion.commit()
            print(f"---> Registro {id}, con fecha {fecha} actualizado correctamente")
        except sqlite3.Error as error:
            print(f"Error a cargar_datos: {error}")
            self.conexion.rollback()
        finally:
            self.desconectar()

class ModeloConfig(MiBaseDeDatosConnect):
#metodos de retorno y grabacion de configuraciones
    def return_config(self,parametro):
        """CONSULA EN LA BASE DE DATOS, DEPENDIENDO DEL PARAMETRO EN LA TABLA CONFIGURACION

        Args:
            parametro (STR): 'color_fondo','link_afip'

        Returns:
            str: config_txt_valor 
        """            
        self.conectar()
        try:
            sql = """
                SELECT config_txt_valor 
                FROM config_app 
                WHERE config_txt_tipo = ?
            """
            data = (parametro,)
            self.cursor.execute(sql, data)
            retorno = (self.cursor.fetchall()[0][0])
            print("---> Configuracion retornada con exito metodo: return_config()")
            return retorno
        except sqlite3.Error as error:
            print(f"Error a retornar {parametro}: {error}")
            self.conexion.rollback()
        finally:
            self.desconectar()

    def grabar_config(self,config_txt_tipo, cinfig_txt_valor):
        """GRABA UNA NUEVA CONFIGURACION

        Args:
            config_txt_tipo (STR): 'color_fondo','link_afip'
            cinfig_txt_valor (STR): nuevo_valor
        """            
        self.conectar()
        try:
            sql = """
                UPDATE config_app
                SET config_txt_valor = ?
                WHERE config_txt_tipo = ?
            """
            data = (cinfig_txt_valor,config_txt_tipo,)
            self.cursor.execute(sql, data)
            print(f"---> Configuracion {config_txt_tipo} grabada exitosamente")
        except sqlite3.Error as error:
            print(f"Error a retornar {cinfig_txt_valor,config_txt_tipo}: {error}")
            self.conexion.rollback()
        finally:
            self.desconectar()

#metodos de retorno y grabacion de conceptos
    def return_conceptos(self):
        self.conectar()
        try:
            sql = """
                SELECT *
                FROM conceptos
                WHERE con_txt_estado = 'activo'
                """ 
            self.cursor.execute(sql)
            retorno = (self.cursor.fetchall())
            print("---> Conceptos retornados con exito metodo:return_conceptos()")
            return retorno
        except sqlite3.Error as error:
            print(f"Error a retornar conceptos: {error}")
            self.conexion.rollback()
        finally:
            self.desconectar()

    def agrega_concepto(self,concepto):
        self.conectar()
        try:
            sql = """
                INSERT INTO conceptos (con_txt_descripcion , con_txt_estado) 
                SELECT ?,?
                WHERE NOT EXISTS (SELECT 1 FROM conceptos WHERE con_txt_descripcion = ?)
            """
            data = (concepto,"activo",concepto)
            self.cursor.execute(sql,data)
            self.conexion.commit()
            print("---> Conceptos agregados con exito metodo:agrega_conceptos()")
        except sqlite3.Error as error:
                    print(f"Error a grabar {concepto}: {error}")
                    self.conexion.rollback()
        finally:
            self.desconectar()

    def borra_concepto(self,concepto):
        self.conectar()
        try:
            sql = """
                DELETE FROM conceptos WHERE con_txt_descripcion = ?
            """
            data = (concepto,)
            self.cursor.execute(sql,data)
            self.conexion.commit()
            print("---> Concepto eliminado con exito metodo:borra_conceptos()")
        except sqlite3.Error as error:
                    print(f"Error a eliminar {concepto}: {error}")
                    self.conexion.rollback()
        finally:
            self.desconectar()

class Estadisticas(MiBaseDeDatosConnect):
        def calculos_total_facturas(self,mes):
            self.conectar()
            sql_total_facturas = ("SELECT COUNT(*) FROM Facturacion WHERE substr(fac_date_fecha, 6, 2) = ?")
            self.cursor.execute(sql_total_facturas,(mes,))
            self.conexion.commit()
            
            total_facturas=self.cursor.fetchall()
        
            concatenar = str(total_facturas[0][0]) # Aca exraigo solo al primer numero del fetchall y le saco la ,
            self.desconectar()
            return concatenar
        
        def facturado_mes_actual(self,mes):
            self.conectar()
            sql_facturado_este_mes =("SELECT SUM(fac_bol_monto) FROM Facturacion WHERE substr(fac_date_fecha, 6, 2) = ?")
            self.cursor.execute(sql_facturado_este_mes,(mes,))
            self.conexion.commit()
            facturado_este_mes=self.cursor.fetchone()
            return facturado_este_mes

        def total_facturado_periodo(self,):
            fecha = "2023/1/1"
            
            self.conectar()
            sql_facturado_este_periodo =("SELECT SUM(fac_bol_monto) FROM Facturacion WHERE fac_date_fecha > ?")
            self.cursor.execute(sql_facturado_este_periodo,(fecha,))
            self.conexion.commit()
            facturado_este_periodo=self.cursor.fetchone()
            self.monto_facturado = facturado_este_periodo

            self.monto_facturado = (facturado_este_periodo)
            return self.monto_facturado

        def falta_facturar_responsable_inscripto(self):
            if self.monto_facturado[0] == None:
                falta_ri = 0 
            else:
                falta_ri = self.categoriaH - self.monto_facturado[0]  
                
                if self.monto_facturado[0] == None:
                    falta_ri = "---------------"
                    return falta_ri
                elif falta_ri < 0:
                    falta_ri = "Te pasaste"
                    return falta_ri
                else:
                    return falta_ri
                
        def facturado_anual(self):
            año_actual = datetime.datetime.now().year
            primer_dia_año = datetime.datetime(año_actual, 1, 1)
           

            self.conectar()
            sql_facturado_este_anio =("SELECT SUM(fac_bol_monto) FROM Facturacion WHERE fac_date_fecha > ?")
            self.cursor.execute(sql_facturado_este_anio,(primer_dia_año,))
            self.conexion.commit()
            facturacion_anual=self.cursor.fetchone()
            return facturacion_anual


        def devolver_categorias(self):
            #CATEGORIA A
            self.conectar()
            sqlA = "SELECT * FROM categoria_monotributo where cat_txt_descripcion='A';"
            self.cursor.execute(sqlA)
            self.conexion.commit()
            rows = self.cursor.fetchall()
            for x in rows:
                self.categoriaA=x[2]
            
            #CATEGORIA B
            self.conectar()
            sqlB = "SELECT * FROM categoria_monotributo where cat_txt_descripcion='B';"
            self.cursor.execute(sqlB)
            self.conexion.commit()
            rows = self.cursor.fetchall()
            for x in rows:
                self.categoriaB=x[2]

            #CATEGORIA C
            self.conectar()
            sqlC = "SELECT * FROM categoria_monotributo where cat_txt_descripcion='C';"
            self.cursor.execute(sqlC)
            self.conexion.commit()
            rows = self.cursor.fetchall()
            for x in rows:
                self.categoriaC=x[2]

            #CATEGORIA D
            self.conectar()
            sqlD = "SELECT * FROM categoria_monotributo where cat_txt_descripcion='D';"
            self.cursor.execute(sqlD)
            self.conexion.commit()
            rows = self.cursor.fetchall()
            for x in rows:
                self.categoriaD=x[2]
            
            #CATEGORIA E
            self.conectar()
            sqlE = "SELECT * FROM categoria_monotributo where cat_txt_descripcion='E';"
            self.cursor.execute(sqlE)
            self.conexion.commit()
            rows = self.cursor.fetchall()
            for x in rows:
                self.categoriaE=x[2]

            #CATEGORIA F
            self.conectar()
            sqlF = "SELECT * FROM categoria_monotributo where cat_txt_descripcion='F';"
            self.cursor.execute(sqlF)
            self.conexion.commit()
            rows = self.cursor.fetchall()
            for x in rows:
                self.categoriaF=x[2]

            #CATEGORIA G
            self.conectar()
            sqlG = "SELECT * FROM categoria_monotributo where cat_txt_descripcion='G';"
            self.cursor.execute(sqlG)
            self.conexion.commit()
            rows = self.cursor.fetchall()
            for x in rows:
                self.categoriaG=x[2]

            #CATEGORIA H
            self.conectar()
            sqlH = "SELECT * FROM categoria_monotributo where cat_txt_descripcion='H';"
            self.cursor.execute(sqlH)
            self.conexion.commit()
            rows = self.cursor.fetchall()
            for x in rows:
                self.categoriaH=x[2]



            return self.categoriaA,\
                    self.categoriaB,\
                        self.categoriaC,\
                            self.categoriaD,\
                                self.categoriaE,\
                                    self.categoriaF,\
                                        self.categoriaG,\
                                            self.categoriaH





class Validador():
    
    def valida_concepto (self,valido_concepto):
        if valido_concepto == "" or valido_concepto == "Agregar Nuevo" or valido_concepto == ("--"*5) or valido_concepto =="Eliminar Concepto":
            print("error al validar concepto")
            return "ERROR"
        
        
    def valida_monto(self,texto):
        patron = r"^\d+(\.\d+)?$" #Valida numeros enteros y decimales.
        cadena =  texto
        if re.match (patron,cadena):
            return "OK"
        else:
            return "ERROR"
    

    
    def valida_fecha(self,valido_fecha):
        if valido_fecha == "":
            return "ERROR"



#ESTO ES PARA PRUEBAS
if __name__ == "__main__":
    # Uso de la clase Factura
    mibase = MiBaseDeDatosConnect()
    mibase.carga_datos_iniciales()
    print(mibase.actualizar_treeview())
    #print("si le pido a la funcion link_afip, me devuelve:" , mibase.return_config('link_afip'))
    #print("si le pido a la funcion color_fondo, me devuelve:" , mibase.return_config('color_fondo'))


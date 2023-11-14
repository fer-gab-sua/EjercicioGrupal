import sqlite3

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

                sql = """
                INSERT INTO config_app (config_txt_tipo , config_txt_valor) 
                SELECT ?,?
                WHERE NOT EXISTS (SELECT 1 FROM config_app WHERE config_txt_tipo = 'color_fondo')
                """
                data = ('color_fondo','#004080')
                self.cursor.execute(sql, data)

                self.conexion.commit()
                print("datos cargados correctamente")
            except sqlite3.Error as error:
                print(f"Error en la carga inicial: {error}")
                self.conexion.rollback()

    def modificar_factura(self,factura_id, nueva_fecha, nuevo_id_concepto, nuevo_monto, nuevo_cuil_cliente):
        """MODIFICA UNA FACTURA EXISTENTE EN LA BASE DE DATOS

        Args:
            factura_id (_int_): _factura a modificar_
            nueva_fecha (_date_): _nueva fecha_
            nuevo_id_concepto (_int_): _nuevo id concepto_
            nuevo_monto (_bol_): _nuevo monto_
            nuevo_cuil_cliente (_str_): _nuevo cuil de cliente_
        """        
        try:
            self.conectar()
            sql = "UPDATE facturacion SET fac_date_fecha = ?, fac_int_idconcepto = ?, fac_bol_monto = ?, fac_txt_cuilcliente = ? WHERE fac_int_id = ?"
            data = (nueva_fecha, nuevo_id_concepto, nuevo_monto, nuevo_cuil_cliente, factura_id)
            self.cursor.execute(sql,data)
            self.conexion.commit()
            print(f"Factura con ID {factura_id} modificada correctamente")
        except sqlite3.Error as error:
            print(f"Error al modificar la factura: {error}")
            self.conexion.rollback()
        
    def borrar_factura(self,factura_id):
        try:
            self.conectar()
            sql = "DELETE FROM facturacion WHERE fac_int_id = ?"
            data = (factura_id,)
            self.cursor.execute(sql,data)
            self.conexion.commit()
            print(f"Factura con ID {factura_id} fue eliminada correctamente ")
        except sqlite3.Error as error:
            print(f"Error al eliminar la factura: {error}")
            self.conexion.rollback()


class Factura():
    def __init__(self, fecha, id_concepto, monto, cuil_cliente):
        self.fecha = fecha
        self.id_concepto = id_concepto
        self.monto = monto
        self.cuil_cliente = cuil_cliente

    def validar_factura(self):
        if not self.fecha or not self.id_concepto or self.monto <= 0 or not self.cuil_cliente:
            return False
        return True
    
    def agregar_a_base_de_datos(self, base_de_datos):
        """AGREGA LA FACTURA A LA BASE DE DATOS

        Args:
            base_de_datos (_obj_): _objeto de base de datos donde tiene que ingresar la fatura_
        """            
        if self.validar_factura():
            try:
                base_de_datos.conectar()
                sql = "INSERT INTO facturacion (fac_date_fecha, fac_int_idconcepto, fac_bol_monto, fac_txt_cuilcliente) VALUES (?,?,?,?)"
                data = (self.fecha, self.id_concepto, self.monto, self.cuil_cliente)
                base_de_datos.cursor.execute(sql, data)
                base_de_datos.conexion.commit()
                print("Factura agregada correctamente a la base de datos")
            except sqlite3.Error as error:
                print(f"Error al agregar la factura a la base de datos: {error}")
                base_de_datos.conexion.rollback()
        else:
            print("Factura no válida. No se ha agregado a la base de datos")


if __name__ == "__main__":
    # Uso de la clase Factura
    mibase = MiBaseDeDatos()

    mibase.carga_datos_iniciales()

    nueva_factura = Factura('2023-11-08', 1, 100.0, '1234567890')
    nueva_factura.agregar_a_base_de_datos(mibase)


    mibase.modificar_factura()

    nueva_factura.agregar_a_base_de_datos()


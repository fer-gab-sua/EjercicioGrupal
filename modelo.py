"""MODELO CREADO PARA INTERACTUAR CON LA VISTA GRABANDO LOS DATOS Y RETORNANDOLOS EN UNA BASE SQLITE3
"""

import sqlite3
import re
import pandas as pd
from tkinter import filedialog

__author__ = "Fernando Suarez, Damian Colomb"
__mainteinter__ = "Fernando Suarez, Damian Colomb"
__email__ = "fer.gab.sua@gmail.com , colomb.damian@gmail.com"
__copyrigth__ = "Copyright 2023"
__version__ = "0.1"


class MiBaseDeDatosConnect():
    """Clase para gestionar la conexión y manipulación de la base de datos.
    """
    def __init__(self, nombre_base_de_datos = "facturacion.db"):
        """Inicializa la conexión y crea las tablas si no existen.

        Args:
            nombre_base_de_datos (str, optional): Nombre de la base de datos. por defectp: "facturacion.db".
        """        
        self.nombre_base_de_datos = nombre_base_de_datos
        self.conexion = None
        self.cursor = None
        self.crear_tablas()

    def conectar(self):
        """Establece una conexión con la base de datos.
        """
        try:
            self.conexion = sqlite3.connect(self.nombre_base_de_datos)
            self.conexion.isolation_level = None  # Desactiva el autocommit
            self.cursor = self.conexion.cursor()
            print("-> Conexión abierta")
        except sqlite3.Error as error:
            print(f"Error al conectar a la base de datos: {error}")

    def desconectar(self):
        """Cierra la conexión con la base de datos.
        """
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()
            print("-> Conexión cerrada")
            print("\n")

    def crear_tablas(self):
        """Crea las tablas necesarias si no existen.
        """
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
    """Clase para gestionar categorías en la base de datos.
    """
    def traer_categorias(self):
        """Retorna las categorías de monotributo.

        Returns:
            list: Lista de categorías.
        """
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
        """Agrega categorías a la base de datos.

        Args:
            bloque (list): Lista de categorías a agregar.
        """
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
    """Clase para obtener datos para la interfaz de usuario.
    """
    def actualizar_treeview(self,anio):
        """Actualiza el treeview con datos de facturación para el año dado.

        Args:
            anio (int): Año de interés.

        Returns:
            list: Datos para el treeview.
        """
        self.conectar()
        print("voy a filtrar por ---->",anio)
        try:
            sql_treeview = """SELECT * 
                        FROM facturacion 
                        WHERE substr(fac_date_fecha, 1, 4) = ?
                        ORDER BY fac_date_fecha ASC"""
            self.cursor.execute(sql_treeview, (anio,))
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
        """Calcula la suma total de facturación.

        Returns:
            float: Suma total de facturación.
        """
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
    """Clase para realizar operaciones CRUD en la base de datos.
    """
    def cargar_datos(self,fecha,concepto,monto,instante):
        """Carga nuevos datos de facturación en la base de datos.

        Args:
            fecha (str): Fecha de la factura.
            concepto (str): Concepto de la factura.
            monto (float): Monto de la factura.
            instante (str): Fecha y hora de la operación.
        """
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
        """Elimina un registro de facturación de la base de datos.

        Args:
            borrar (int): ID del registro a eliminar.
        """
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
        """Actualiza un registro de facturación en la base de datos.

        Args:
            fecha (str): Nueva fecha de la factura.
            concepto (str): Nuevo concepto de la factura.
            monto (float): Nuevo monto de la factura.
            id (int): ID del registro a actualizar.
        """
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
    """Clase para gestionar configuraciones en la base de datos.
    """
    def return_config(self,parametro):
        """Consulta la configuración en la base de datos.

        Args:
            parametro (str): 'color_fondo' o 'link_afip'.

        Returns:
            str: Valor de la configuración.
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
        """Graba una nueva configuración en la base de datos.

        Args:
            config_txt_tipo (str): 'color_fondo' o 'link_afip'.
            config_txt_valor (str): Nuevo valor de la configuración.
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
        """Retorna los conceptos para agregar a la lista

        Returns:
            list: Lista de conceptos
        """
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
        """Agrega un nuevo concepto a la base de datos.

        Args:
            concepto (str): Nuevo concepto a agregar.
        """
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
        """Elimina un concepto de la base de datos.

        Args:
            concepto (str): Concepto a eliminar.
        """
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
        """Clase para realizar cálculos y estadísticas en la base de datos.
        """
        def calculos_total_facturas(self,anio_fiscal):
            """Calcula el total de facturas para un año fiscal.

            Args:
                anio_fiscal (int): Año fiscal de interés.

            Returns:
                int: Total de facturas.
            """
            print("EL AÑO FISCAL ES:",anio_fiscal)
            
            self.fecha_ini = (str(anio_fiscal)+"/1/1")
            self.fecha_fin = (str(anio_fiscal)+"12/31")

            self.conectar()
            sql_total_facturas = ("SELECT COUNT(*) FROM Facturacion WHERE fac_date_fecha > ? and fac_date_fecha < ?")
            self.cursor.execute(sql_total_facturas,(self.fecha_ini, self.fecha_fin))
            self.conexion.commit()
            
            total_facturas=self.cursor.fetchone()
        
            concatenar = (total_facturas[0]) # Aca exraigo solo al primer numero del fetchall y le saco la ,
            print("---> Select calculo total ejecutado correctamente()")
            self.desconectar()
            return concatenar
        
        def facturado_mes_actual(self,mes):

            """Calcula el monto facturado en el mes actual.

            Args:
                mes (str): Mes de interés (formato 'MM').

            Returns:
                float: Monto facturado en el mes actual.
            """
            
            self.conectar()
            sql_facturado_este_mes =("SELECT SUM(fac_bol_monto) FROM Facturacion WHERE substr(fac_date_fecha, 6, 2) = ?")
            self.cursor.execute(sql_facturado_este_mes,(mes,))
            self.conexion.commit()
            facturado_este_mes=self.cursor.fetchone()
            print("---> Select facturo mes actual ejecutado correctamente()")
            self.desconectar()
            
            return facturado_este_mes

        def total_facturado_periodo(self,):
            """Calcula el total facturado en el período actual.

            Returns:
                float: Monto total facturado en el período actual.
            """
            self.conectar()
            sql_facturado_este_periodo =("SELECT SUM(fac_bol_monto) FROM Facturacion WHERE fac_date_fecha > ? and fac_date_fecha < ?")
            self.cursor.execute(sql_facturado_este_periodo,(self.fecha_ini,self.fecha_fin))
            self.conexion.commit()
            facturado_este_periodo=self.cursor.fetchone()
            self.monto_facturado = facturado_este_periodo

            self.monto_facturado = (facturado_este_periodo)
            print("---> Select total facturado por periodo ejecutado correctamente()")
            self.desconectar()
            return self.monto_facturado

        def falta_facturar_responsable_inscripto(self):
            """Calcula la cantidad que falta facturar para alcanzar la categoría H.

            Returns:
                int/str: Cantidad faltante o mensaje de error.
            """
            if self.monto_facturado[0] == None:
                falta_ri = 0 
            else:
                falta_ri = self.categoriaH - self.monto_facturado[0]  
                
                if self.monto_facturado[0] == None:
                    falta_ri = "error"
                    return falta_ri
                elif falta_ri < 0:
                    falta_ri = "negativo"
                    return falta_ri
                else:
                    return falta_ri
                
        def facturado_anual(self,primer_dia_año):
            """Calcula el monto total facturado en el año.

            Args:
                primer_dia_anio (str): Primer día del año (formato 'YYYY/MM/DD').

            Returns:
                float: Monto total facturado en el año.
            """
            ## Pasar a la vista
            
           

            self.conectar()
            sql_facturado_este_anio =("SELECT SUM(fac_bol_monto) FROM Facturacion WHERE fac_date_fecha > ?")
            self.cursor.execute(sql_facturado_este_anio,(primer_dia_año,))
            self.conexion.commit()
            facturacion_anual=self.cursor.fetchone()
            print("---> Select facturado anual ejecutado correctamente()")
            self.desconectar()
            return facturacion_anual

        def devolver_categorias(self):
            """Devuelve los montos asociados a cada categoría.

            Returns:
                tuple: Montos de las categorías A-H.
            """
            print("Bloque de select para devolver categoria")
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
            self.desconectar()  
            print("fin bloque categorias")
            

            return self.categoriaA,\
                    self.categoriaB,\
                        self.categoriaC,\
                            self.categoriaD,\
                                self.categoriaE,\
                                    self.categoriaF,\
                                        self.categoriaG,\
                                            self.categoriaH
        
        def exportar(self):
            """Exporta los datos de facturación a un archivo Excel.
            """
            self.conectar()
            sql= "SELECT * FROM Facturacion"
            exportar = pd.read_sql_query(sql,self.conexion)
            ruta = filedialog.asksaveasfilename(defaultextension='.xlsx')
            exportar.to_excel(ruta,index=False)
            self.desconectar()




class Validador():
    """Clase con métodos para validar datos ingresados.
    """
    def valida_concepto (self,valido_concepto):
        """Valida que el concepto ingresado sea válido.

        Args:
            valido_concepto (str): Concepto a validar.

        Returns:
            str: "OK" si es válido, "ERROR" si no es válido.
        """
        if valido_concepto == "" or valido_concepto == "Agregar Nuevo" or valido_concepto == ("--"*5) or valido_concepto =="Eliminar Concepto":
            print("error al validar concepto")
            return "ERROR"
        
        
    def valida_monto(self,texto):
        """Valida que el formato del monto sea válido.

        Args:
            texto (str): Monto a validar.

        Returns:
            str: "OK" si es válido, "ERROR" si no es válido.
        """
        patron = r"^\d+(\.\d+)?$" #Valida numeros enteros y decimales.
        cadena =  texto
        if re.match (patron,cadena):
            return "OK"
        else:
            return "ERROR"
    

    
    def valida_fecha(self,valido_fecha):
        """Valida que la fecha ingresada sea válida.

        Args:
            valido_fecha (str): Fecha a validar.

        Returns:
            str: "OK" si es válida, "ERROR" si no es válida.
        """
        if valido_fecha == "":
            return "ERROR"

    def valida_entero(self, texto):
        """Valida que el formato del número entero sea válido.

        Args:
            texto (str): Número entero a validar.

        Returns:
            str: "OK" si es válido, "ERROR" si no es válido.
        """

        patron = r"^\d{4}$"
        cadena = texto
        if re.match(patron, cadena):
            return "OK"
        else:
            return "ERROR"


#ESTO ES PARA PRUEBAS
if __name__ == "__main__":
    # Uso de la clase Factura
    estadistiacas = Estadisticas()
    estadistiacas.exportar()
    
    #print("si le pido a la funcion link_afip, me devuelve:" , mibase.return_config('link_afip'))
    #print("si le pido a la funcion color_fondo, me devuelve:" , mibase.return_config('color_fondo'))


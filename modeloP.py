from peewee import *
from datetime import datetime


namebase = "facturacionNueva.db"
db = SqliteDatabase(namebase)

class BaseModel(Model):
    class Meta:
        database = db

class Factura(BaseModel):
    fac_int_id = AutoField(unique=True)
    fac_date_fecha = DateField()
    fac_txt_concepto = CharField()
    fac_bol_monto = FloatField() 
    instante = DateTimeField() 
    

db.connect()
db.create_tables([Factura])

class MiBaseDeDatosNw():
    def __init__(self) -> None:
        pass


    def cargar_datos(self, fecha, concepto, monto, instante=None):
        factura = Factura()
        factura.fac_date_fecha = fecha
        factura.fac_txt_concepto = concepto
        factura.fac_bol_monto = monto
        factura.instante = instante or datetime.now()  
        factura.save()

    def borrar_datos(self,borrar):
        obj_borrar = Factura.get(Factura.get(Factura.fac_int_id==borrar))
        obj_borrar.delete_instance()


    def actualizar_datos(self,act_fecha,act_concepto,act_monto,id_factura, instante = None):
        factura_mod = Factura.update(fac_date_fecha=act_fecha , fac_txt_concepto = act_concepto, fac_bol_monto = act_monto).where(Factura.fac_int_id==id_factura)
        factura_mod.execute()




    def actualizar_treeview(self):
        datos = []
        for fila in Factura.select():
            datos.append((fila.fac_int_id,
                        fila.fac_date_fecha, 
                        fila.fac_txt_concepto, 
                        fila.fac_bol_monto))
        return datos

mibase = MiBaseDeDatosNw()
print(mibase.actualizar_treeview())

mibase.actualizar_datos("fecha","concepto",20.3,4)
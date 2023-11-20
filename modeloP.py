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

class MiBaseDeDatos():
    def __init__(self) -> None:
        pass


    def alta(self, fecha, concepto, monto, instante=None):
        factura = Factura()
        factura.fac_date_fecha = fecha
        factura.fac_txt_concepto = concepto
        factura.fac_bol_monto = monto
        factura.instante = instante or datetime.now()  
        factura.save()

    def actualizar_treeview(self):
        datos = Factura.select()
        return datos

mibase = MiBaseDeDatos()
mibase.alta("01/01/2023","coco","12.5")
print(mibase.actualizar_treeview())
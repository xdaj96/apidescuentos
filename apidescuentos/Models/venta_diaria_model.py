from peewee import IntegerField,TextField,BooleanField,Model,DateTimeField,DecimalField,Model
from database import db

class VentaDiaria(Model):
    cod_alfabeta = IntegerField()
    fecha = DateTimeField()
    sucursal_id = IntegerField()
    venta_pesos = DecimalField()
    cantidad = IntegerField()
    
    class Meta:
        database = db
        table_name='ventadiaria'
        
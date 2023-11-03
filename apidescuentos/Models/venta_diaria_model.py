from peewee import Model,IntegerField,TextField,FloatField,DateField
from database import db
class VentaDiaria(Model):
    fecha = DateField()
    sucursal_id = TextField()
    cantidad = IntegerField()
    cod_alfabeta = IntegerField()
    cod_rubro = TextField()
    cod_laboratorio = TextField()
    
    venta_pesos= FloatField()
    costo_pesos = FloatField()
    nro_comprobante = IntegerField()
    
    
    class Meta:
        database = db
        table_name='ventadiaria'
    
    def to_dict(self):
        return {
            "cod_planos":self.cod_laboratorio,
            "nom_planos":self.cod_rubro
        }
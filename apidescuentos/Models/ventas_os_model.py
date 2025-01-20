from peewee import Model,IntegerField,TextField,FloatField,DateField
from database import dbAutodw
class VentasOS(Model):
    fecha = DateField()
    sucursal_id = TextField()
    cod_planos = TextField()
    unidades = IntegerField()
    cod_alfabeta = IntegerField()
    importe_pesos= FloatField()
    importe_desc = FloatField()
    tip_comprobante = TextField()
    nro_comprobante = IntegerField()
    
    
    class Meta:
        database = dbAutodw
        table_name='ventadiariaos'
    
    def to_dict(self):
        return {
            "cod_planos":self.cod_planos,
            "nom_planos":self.nom_planos
        }
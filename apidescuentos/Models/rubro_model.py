from peewee import Model,IntegerField,TextField,FloatField
from database import db
class Rubro(Model):
    cod_rubro = TextField(primary_key=True)
    des_rubro = TextField()
    cod_grupo  = TextField()
    des_grupo  = TextField()
    por_margen  = FloatField()

    class Meta:
        database = db
        table_name='prmarubro'
    
    def to_dict(self):
        return {
            "cod_rubro":self.cod_rubro,
            "des_rubro":self.des_rubro,
            "cod_grupo": self.cod_grupo,
            "des_grupo": self.des_grupo,
            "por_margen":self.por_margen
        }
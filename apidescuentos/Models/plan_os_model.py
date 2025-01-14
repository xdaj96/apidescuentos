from peewee import Model,IntegerField,TextField
from database import db
class PlanOS(Model):
    cod_planos = TextField()
    nom_planos = TextField()
    cod_grupo  = TextField()
    
    class Meta:
        database = db
        table_name='planes_os'
    
    def to_dict(self):
        return {
            "cod_planos":self.cod_planos,
            "nom_planos":self.nom_planos
        }
from peewee import Model,TextField,FloatField
from database import db
class Laboratorio(Model):
    cod_laboratorio = TextField(primary_key=True)
    nom_laboratorio = TextField()
    margen  = FloatField()
    
    class Meta:
        database = db
<<<<<<< Updated upstream
        table_name='prmalaboratorio'
=======
        table_name='prmalaboratorio' 
>>>>>>> Stashed changes
    
    def to_dict(self):
        return {
            "cod_laboratorio":self.cod_laboratorio,
            "nom_laboratorio":self.nom_laboratorio,
            "margen": self.margen,
 
        }
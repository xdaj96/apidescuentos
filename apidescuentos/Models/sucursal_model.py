
from peewee import Model,TextField,IntegerField 
from database import db 

class Sucursal(Model):
    sucursal_id = IntegerField(primary_key=True)
    nom_sucursal = TextField()
    nro_sucursal = IntegerField()
    razon_social = TextField()
    cuit = TextField()
    direccion = TextField()
    ciudad = TextField()
    provincia = TextField()    
    activa =  TextField()
    
    def to_dict(self) ->dict: 
        return {
            "sucursal_id": self.sucursal_id,
            "nom_sucursal": self.nom_sucursal,
            "nro_sucursal":self.nro_sucursal,
            "razon_social":self.razon_social,
            "cuit": self.cuit,
            "direccion": self.direccion,
            "ciudad": self.ciudad,
            "provincia": self.provincia,
            "activa": self.activa 
        }
    class Meta:
        database = db
        table_name='sucursal'
        

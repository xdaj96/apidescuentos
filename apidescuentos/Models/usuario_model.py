from peewee import IntegerField,TextField,BooleanField,Model
from database import db
class Usuario(Model):
    
    usuario_id = IntegerField(primary_key=True)
    nombre_usuario = TextField()
    nombre = TextField()
    apellido = TextField()
    acceso_total = BooleanField()
    email = TextField()
    password = TextField()
    
    
  
    def nombreCompleto(self):
        return self.nombre + ' ' + self.apellido
    
    def tieneAccesoTotal(self): 
        return self.acceso_total
    
    def to_dict(self):
        return {
            'id_usuario':self.usuario_id,
            'nombre': self.nombreCompleto(),
            'acceso_total': self.acceso_total,
            'email': self.email,
            'usuario': self.nombre_usuario
            
        }

    class Meta:
        database = db
        db_table = 'usuario'
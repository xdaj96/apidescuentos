
from peewee import Model,TextField,IntegerField,DateField,ForeignKeyField,FloatField
from database import db 
from Models.sucursal_model import Sucursal
from datetime import datetime

class DescuentoEsquema(Model):
    descuento_esquema_id = IntegerField(primary_key=True)
    nombre = TextField()
    fecha_vig_inicio = DateField()
    fecha_vig_fin = DateField()
    tipo = TextField()
    monto_porcentaje = FloatField()
    dias_semana = TextField()
    cupon = TextField()    
    sucursal_id = ForeignKeyField(Sucursal,backref='descuento_esquema', to_field='sucursal_id')
    created_at = DateField()
    
    
    
    def to_dict(self) ->dict:
         
        descuento_dict =  {
            "descuento_esquema_id": self.descuento_esquema_id,
            "nombre": self.nombre,
            "fecha_vig_inicio":self.fecha_vig_inicio,
            "fecha_vig_fin":self.fecha_vig_fin,
            "sucursal_id": 0,
            "sucursal": "TODAS",
            "dias_semana": self.dias_semana,
            "cupon": self.cupon,
            "tipo": self.tipo,
            "monto_porcentaje":self.monto_porcentaje
        }
        try: 
            descuento_dict['sucursal'] = self.sucursal_id.nom_sucursal
            descuento_dict['sucursal_id'] = self.sucursal_id.sucursal_id
        except Sucursal.DoesNotExist:
            descuento_dict['sucursal'] ="TODAS"
            descuento_dict['sucursal_id'] = 0
            
        
        
        return descuento_dict
    
    class Meta:
        database = db
        table_name='descuento_esquema'
        
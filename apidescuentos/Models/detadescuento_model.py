
from peewee import Model,TextField,IntegerField,DateField,ForeignKeyField,FloatField
from database import db 
from Models.sucursal_model import Sucursal
from Models.producto_model import Producto
from Models.plan_os_model import PlanOS
from datetime import datetime

class DescuentoDetalle(Model):
    descuento_detalle_id = IntegerField(primary_key=True)
    descuento_esquema_id = IntegerField()
    cod_alfabeta = IntegerField()
    cod_rubro = IntegerField()
    cod_laboratorio = IntegerField()
    cod_planos = TextField()
    sucursal_id = IntegerField()
    condicion_venta = TextField()
    repeticion = IntegerField()
    cantidad = IntegerField()
    tipo = TextField()
    porcentaje_descuento = FloatField()
    importe_fijo = FloatField()
    tipo = TextField()
    producto = ForeignKeyField(Producto, to_field='cod_alfabeta', backref='descuento_detalle', column_name='cod_alfabeta')
    plan_os = ForeignKeyField(PlanOS, to_field='cod_planos', backref='descuento_detalle', column_name='cod_planos')
    
    # Método to_dict para convertir el objeto en un diccionario
    def to_dict(self):
        detalleDict =  {
            "descuento_detalle_id": self.descuento_detalle_id,
            "descuento_esquema_id": self.descuento_esquema_id,
            "cod_rubro": self.cod_rubro,
            "cod_laboratorio": self.cod_laboratorio,
            "cod_planos": self.cod_planos,
            "cod_alfabeta": self.cod_alfabeta,
             
            "sucursal_id": self.sucursal_id,
            "condicion_venta": self.condicion_venta,
            "repeticion": self.repeticion,
            "cantidad": self.cantidad,
            "tipo": self.tipo,
            "porcentaje_descuento": self.porcentaje_descuento,
            "importe_fijo": self.importe_fijo
        }
        try: 
            detalleDict['producto'] = self.producto.to_dict()
            
        except Producto.DoesNotExist:
            detalleDict['producto'] ={}
          
        try: 
            detalleDict['plan_os'] = self.plan_os.to_dict()
            
        except PlanOS.DoesNotExist:
            detalleDict['plan_os'] ={}
            
        
         
        return detalleDict    
        
        
    class Meta:
        database = db
        table_name='descuento_detalle'
        
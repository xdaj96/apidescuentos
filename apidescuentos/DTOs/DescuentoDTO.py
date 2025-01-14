from Models.descuento_model import DescuentoEsquema 
class DescuentoEsquemaDTO():
    def __init__(self, model: DescuentoEsquema):        
        self.descuento_esquema_id=model.descuento_esquema_id,
        self.nombre=model.nombre,
        self.fecha_vig_inicio=model.fecha_vig_inicio,
        self.fecha_vig_fin=model.fecha_vig_fin,
        self.tipo=model.tipo,
        self.monto_porcentaje=model.monto_porcentaje,
        self.sucursal_id=model.sucursal_id
        self.nom_sucursal=''
        self.dias_semana = model.dias_semana
        self.cupon = model.cupon
    @classmethod
    def from_model(cls,model:DescuentoEsquema):
        return cls(
            model
        )
    
    def to_dict(self):
        return  {
            "descuento_esquema_id": self.descuento_esquema_id,
            "nombre": self.nombre,
            "fecha_vig_inicio":self.fecha_vig_inicio,
            "fecha_vig_fin":self.fecha_vig_fin,
            "sucursal_id": self.sucursal_id,
            "dias_semana": self.dias_semana,
            "cupon": self.cupon,
            "tipo": self.tipo,
            "monto_porcentaje":self.monto_porcentaje
        }
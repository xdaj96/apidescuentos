 
from marshmallow import Schema, fields, ValidationError,validates, EXCLUDE
from marshmallow.validate import Length
from validations.validar_detalle_descuento import DetalleDescuentoValidationSchema

class String(fields.String):
    default_error_messages = {"required": "El campo es obligatorio"}


class DescuentoValidationEsquema(Schema):
    nombre = String(min=3, required=True, error_messages={'Length':'La longitud del capo debe ser mayor'})  # Valida que el nombre tenga al menos 3 caracteres
    fecha_vig_inicio = fields.Date(required=True)
    fecha_vig_fin = fields.Date(required=True)
    tipo = String(required=True)
    sucursal_id = fields.Int(required=True)
    monto_porcentaje = fields.Float(required=True)
    dias_semana = String(required=True)
    cupon = String(required=True)
    detalle = fields.List(fields.Nested(DetalleDescuentoValidationSchema),required=True)


    @validates('tipo')
    def validate_tipo(self, value):
        if value not in ['POR', 'FIJ']:
            raise ValidationError("El tipo de descuento debe ser 'FIJO (FIJ)' o 'POR porcentaje (POR)'")

    @validates('fecha_vig_inicio')
    def validate_fecha_vig_inicio(self, value):
        if 'fecha_vig_fin' in self.context and value > self.context['fecha_vig_fin']:
            raise ValidationError("La fecha de inicio no puede ser posterior a la fecha de fin.")

    @validates('fecha_vig_fin')
    def validate_fecha_vig_fin(self, value):
        if 'fecha_vig_inicio' in self.context and value < self.context['fecha_vig_inicio']:
            raise ValidationError("La fecha de fin no puede ser anterior a la fecha de inicio.")

    @validates('nombre')
    def validate_nombre(self, value):
        if len(value) < 3:
            raise ValidationError("El nombre debe tener al menos 3 caracteres.")
        
    @validates('cupon')
    def validar_cupon(self,value):
        if not(value in ['S','N']):
            raise ValidationError("El campo cupon debe ser S o N")

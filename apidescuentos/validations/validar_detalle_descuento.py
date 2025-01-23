
from marshmallow import Schema,fields,ValidationError
class DetalleDescuentoValidationSchema(Schema):
    cod_planos = fields.String(allow_none=True)
    cod_laboratorio = fields.String(allow_none=True)
    cod_alfabeta = fields.String(allow_none=True)
    cod_rubro = fields.String(allow_none=True)
    sucursal_id = fields.Int(required=True)
    tipo = fields.String(required=True)
    repeticion = fields.Int(required = True)
    cantidad = fields.Int(required=True)
 
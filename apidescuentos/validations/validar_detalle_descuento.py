
from marshmallow import Schema,fields,ValidationError
class DetalleDescuentoValidationSchema(Schema):
    cod_planos = fields.String()
    cod_laboratorio = fields.String()
    cod_alfabeta = fields.String()
    cod_laboratorio = fields.String()
    sucursal_id = fields.Int(required=True)
    tipo = fields.String(required=True)


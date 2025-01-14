from peewee import Model,TextField,IntegerField,PrimaryKeyField,FloatField,ForeignKeyField
from Models.rubro_model import Rubro
from database import db
class Producto(Model):
    cod_alfabeta = IntegerField(primary_key=True,column_name='cod_alfabeta')
    nom_largo = TextField()
    cod_barraspri = IntegerField()
    nro_troquel = IntegerField()
    cod_rubro = TextField()
    rubro = ForeignKeyField(Rubro, to_field='cod_rubro', backref='descuento_detalle', column_name='cod_rubro')
    
    def to_dict(self) ->dict: 
        dic_producto =  {
            "cod_alfabeta": self.cod_alfabeta,
            "nom_largo": self.nom_largo,
            "cod_barras_pri":self.cod_barraspri,
            "nro_troquel":self.nro_troquel,
            "cod_rubro": self.cod_rubro
        }
        try:
            dic_producto['rubro'] = self.rubro.to_dict()
        except Rubro.DoesNotExist:
            dic_producto['des_rubro'] = ''
        return dic_producto    
        
        
    class Meta:
        database = db
        table_name='prmaproducto'
        

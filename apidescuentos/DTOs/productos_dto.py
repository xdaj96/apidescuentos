from Models.producto_model import Producto 
class ProductoDTO():
    def __init__(self, model: Producto):        
        self.cod_alfabeta = model.cod_alfabeta
        self.nom_largo = model.nom_largo 
        self.nro_troquel = model.nro_troquel
        self.cod_barraspri = model.cod_barraspri
    @classmethod
    def from_model(cls,model:Producto):
        return cls(
            model
        )
    
    def to_dict(self):
        return  {
            "cod_alfabeta": self.cod_alfabeta,
            "nom_largo": self.nom_largo, 
            "nro_troquel":self.nro_troquel,
            "cod_barraspri":self.cod_barraspri
            
        }
from Models.rubro_model import Rubro 

class RubroDTO():
    def __init__(self, model: Rubro):        
        self.cod_rubro = model.cod_alfabeta
        self.des_rubro = model.nom_largo 
        self.cod_grupo = model.nro_troquel
        self.des_grupo = model.cod_barraspri
        self.por_margen = model.por_margen
        
    @classmethod
    def from_model(cls,model:Rubro):
        return cls(
            model
        )
    
    def to_dict(self):
        return  {
            "cod_rubro":self.cod_rubro,
            "des_rubro":self.des_rubro,
            "cod_grupo": self.cod_grupo,
            "des_grupo": self.des_grupo,
            "por_margen":self.por_margen
        }
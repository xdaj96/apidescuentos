from Models.plan_os_model import PlanOS 
class PlanesOSDTO():
    def __init__(self, model: PlanOS):        
        self.cod_planos=model.cod_planos,
        self.nom_planos=model.nom_planos,
      
    @classmethod
    def from_model(cls,model:PlanOS):
        return cls(
            model
        )
    
    def to_dict(self):
        return  {
            "cod_planos": self.cod_planos,
            "nom_planos": self.nom_planos, 
        }
from Models.plan_os_model import PlanOS 
class LaboratorioDTO():
    def __init__(self, model: PlanOS):        
        self.cod_laboratorio=model.cod_laboratorio,
        self.nom_laboratorio=model.nom_laboratorio,
      
    @classmethod
    def from_model(cls,model:PlanOS):
        return cls(
            model
        )
    
    def to_dict(self):
        return  {
            "cod_laboratorio": self.cod_laboratorio,
            "nom_laboratorio": self.nom_laboratorio, 
        }
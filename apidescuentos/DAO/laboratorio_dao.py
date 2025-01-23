
from DAO.base_dao import BaseDAO
from Models.laboratorio_model import Laboratorio
from DTOs.laboratorio_dto import LaboratorioDTO
class LaboratorioDAO(BaseDAO):
    
    def get_laboratorios(self,filtros ={})->dict:
        
        query = Laboratorio.select(Laboratorio.cod_laboratorio,
            Laboratorio.nom_laboratorio,    
            Laboratorio.margen,
        )
        
        for campo,fieldValue in filtros.items():
            fieldName = getattr(Laboratorio,campo)
            # Si no existe la clave tipo o sea igual filtramos por where simple    
            if fieldValue['tipo'] =='=' or not('tipo' in fieldValue):
                query =query.where(fieldName == fieldValue['valor']) 
                 
            else:
                query = query.where(fieldName.contains(fieldValue['valor']))    
                    
        query = query.order_by(Laboratorio.nom_laboratorio)  # Ordenamos por nombre de laboratorio
        
        
        return LaboratorioDAO.paginated(query, LaboratorioDTO)
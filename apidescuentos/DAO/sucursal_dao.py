from Models.sucursal_model import Sucursal
from typing import List,Optional
from apidescuentos.DAO.base_dao import BaseDAO
from DTOs.sucursal_dto import SucursalDTO
import peewee
class SucursalDAO(BaseDAO):
    
    def __init__(self):
        pass
    
    def get_sucursales(self)->List[Sucursal]:
        return Sucursal.select()
    
    
    def get_sucursales_paginadas(self,filtros ={})->dict:
   
        query = Sucursal.select()
        for campo,fieldValue in filtros.items():
            fieldName = getattr(Sucursal,campo)
            # Si no existe la clave tipo o sea igual filtramos por where simple    
            if fieldValue['tipo'] =='=' or not('tipo' in fieldValue):
                query =query.where(fieldName == fieldValue['valor']) 
                
            else:
                query = query.where(fieldName.contains(fieldValue['valor']))    
                    
        query = query.order_by(Sucursal.nro_sucursal)  # Seleccionamos las sucursales y los ordenamos por nro de sucursal
        
        
        return SucursalDAO.paginated(query,SucursalDTO)
         
    
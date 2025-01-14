from Models.plan_os_model import PlanOS,db
from Models.sucursal_model import Sucursal
from typing import List,Optional
from apidescuentos.DAO.base_dao import BaseDAO
from DTOs.planes_os_dto import PlanesOSDTO

from flask import request
import peewee

class PlanesOSDAO(BaseDAO):
    
    def get_planes_paginados(self,filtros ={})->dict:
        query = PlanOS.select(PlanOS.cod_planos, PlanOS.nom_planos)

        # Filtrar según los filtros
        for campo, fieldValue in filtros.items():
            if campo != 'search':
                fieldName = getattr(PlanOS, campo)
                # Si no existe la clave tipo o es igual, filtramos por where simple    
                if fieldValue.get('tipo') == '=' or 'tipo' not in fieldValue:
                    query = query.where(fieldName == fieldValue['valor'])
                else:
                    query = query.where(fieldName.contains(fieldValue['valor']))    
            else: 
                # Búsqueda por 'search' en cod_planos o nom_planos usando 'OR'
                query = query.where(
                    (PlanOS.cod_planos.contains(fieldValue['valor']))| 
                    (PlanOS.nom_planos.contains(fieldValue['valor']))
                )

        # Ordenar por 'nom_planos'
        query = query.order_by(PlanOS.nom_planos)
       
        # Paginación de los resultados
        return PlanesOSDAO.paginated(query, PlanesOSDTO)
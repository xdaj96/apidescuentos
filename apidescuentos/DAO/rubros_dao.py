from Models.rubro_model import Rubro,db 
from typing import List,Optional
from apidescuentos.DAO.base_dao import BaseDAO
from DTOs.rubro_dto import RubroDTO

from flask import request
import peewee

class RubroDAO(BaseDAO):
    
    def get_rubros_paginados(self,filtros ={})->dict:
        query = Rubro.select()

        # Filtrar según los filtros
        for campo, fieldValue in filtros.items():
            if campo != 'search':
                fieldName = getattr(Rubro, campo)
                # Si no existe la clave tipo o es igual, filtramos por where simple    
                if fieldValue.get('tipo') == '=' or 'tipo' not in fieldValue:
                    query = query.where(fieldName == fieldValue['valor'])
                else:
                    query = query.where(fieldName.contains(fieldValue['valor']))    
            else: 
                # Búsqueda por 'search' en cod_planos o nom_planos usando 'OR'
                query = query.where(
                    (Rubro.cod_rubro.contains(fieldValue['valor'])) | 
                    (Rubro.des_rubro.contains(fieldValue['valor']))  
 
                )

        # Ordenar por 'nom_largo'
        query = query.where(peewee.fn.TRIM( Rubro.des_rubro) != '').order_by(Rubro.des_rubro)
       
        # Paginación de los resultados
        return RubroDAO.paginated(query, RubroDTO)
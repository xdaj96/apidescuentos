from Models.producto_model import Producto,db 
from Models.rubro_model import Rubro
from typing import List,Optional
from apidescuentos.DAO.base_dao import BaseDAO
from DTOs.productos_dto import ProductoDTO

from flask import request
import peewee

class ProductoDAO(BaseDAO):
    
    def get_productos_paginados(self,filtros ={})->dict:
        query = Producto.select(Producto.cod_alfabeta, Producto.cod_barraspri,Producto.nro_troquel,
                                Producto.nom_largo,Rubro.cod_rubro,Rubro.des_rubro).join(Rubro,on=(Producto.cod_rubro == Rubro.cod_rubro))
        # Filtrar según los filtros
        for campo, fieldValue in filtros.items():
            if campo != 'search':
                fieldName = getattr(Producto, campo)
                # Si no existe la clave tipo o es igual, filtramos por where simple    
                if fieldValue.get('tipo') == '=' or 'tipo' not in fieldValue:
                    query = query.where(fieldName == fieldValue['valor'])
                else:
                    query = query.where(fieldName.contains(fieldValue['valor']))    
            else: 
                # Búsqueda por 'search' en cod_planos o nom_planos usando 'OR'
                query = query.where(
                    (Producto.nom_largo.contains(fieldValue['valor']))  
                     
                )

        # Ordenar por 'nom_largo'
        query = query.where(peewee.fn.TRIM( Producto.nom_largo) != '').order_by(Producto.nom_largo)
       
        # Paginación de los resultados
        return ProductoDAO.paginated(query, ProductoDTO)
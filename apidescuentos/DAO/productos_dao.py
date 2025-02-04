from Models.producto_model import Producto,db 
from Models.rubro_model import Rubro
from Models.detadescuento_model import DescuentoDetalle
from Models.descuento_model import DescuentoEsquema
from typing import List,Optional
from apidescuentos.DAO.base_dao import BaseDAO
from DTOs.productos_dto import ProductoDTO

from flask import request
from peewee import fn

class ProductoDAO(BaseDAO):
    
    def get_productos_paginados(self,filtros ={})->dict:
        query = Producto.select(Producto.cod_alfabeta, Producto.cod_barraspri,Producto.nro_troquel,
                                Producto.nom_largo,Rubro.cod_rubro,Rubro.des_rubro).join(Rubro,on=(Producto.cod_rubro == Rubro.cod_rubro))
        # Filtrar según los filtros
        for campo, fieldValue in filtros.items():
            if campo != 'search':
                fieldName = getattr(Producto, campo)
               
                # Si no existe la clave tipo o es igual, filtramos por where simple    
                # Ensure we're casting the value to match the column type
                if 'cod_barraspri' == campo:
                     query = query.where(Producto.cod_barraspri.contains(fieldValue['valor']))
                     print('okas test')
                else:
                    query = query.where(fieldName == fieldValue['valor'])

<<<<<<< Updated upstream
        # Ordenar por 'nom_largo'
        query = query.where(fn.TRIM( Producto.nom_largo) != '').order_by(Producto.nom_largo)
=======
                # Ordenar por 'nom_largo'
                query = query.where(fn.TRIM( Producto.nom_largo) != '').order_by(Producto.nom_largo)
>>>>>>> Stashed changes
       
        # Paginación de los resultados
        return ProductoDAO.paginated(query, ProductoDTO)
    
<<<<<<< Updated upstream
=======
    def obtenerProductoPorCodBarras(self,cod_barraspri) -> Producto:
       return (Producto.get(Producto.cod_barraspri== cod_barraspri))
    
    
    def obtenerProductoPorTroquel(self,nro_troquel) -> Producto:
       return (Producto.get(Producto.nro_troquel== nro_troquel))
    
    
    
    
>>>>>>> Stashed changes
    def getCantProductosConDescuento(self): 
        query = (Producto.select(Producto.cod_alfabeta,Producto.nom_largo).join(DescuentoDetalle, on =(Producto.cod_alfabeta == DescuentoDetalle.cod_alfabeta))
            .join(DescuentoEsquema, on=(DescuentoEsquema.descuento_esquema_id == DescuentoDetalle.descuento_esquema_id))
            .where((fn.NOW() >= DescuentoEsquema.fecha_vig_inicio) & (fn.NOW() <= DescuentoEsquema.fecha_vig_fin))

        )
        
        return query.count()           
 
 
 
    def getCantProductosRegistrados(self):
        query = (Producto.select(Producto.cod_alfabeta,Producto.nom_largo).join(DescuentoDetalle, on =(Producto.cod_alfabeta == DescuentoDetalle.cod_alfabeta))
            .join(DescuentoEsquema, on=(DescuentoEsquema.descuento_esquema_id == DescuentoDetalle.descuento_esquema_id))
        
        )
        
        return query.count() 

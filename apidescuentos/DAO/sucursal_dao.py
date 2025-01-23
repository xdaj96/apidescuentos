from Models.sucursal_model import Sucursal
from Models.descuento_model import DescuentoEsquema
from Models.detadescuento_model import DescuentoDetalle
from typing import List,Optional
from apidescuentos.DAO.base_dao import BaseDAO
from DTOs.sucursal_dto import SucursalDTO
from datetime import date
from peewee import fn 
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
     
    def getCantidadSucursalesActivas(self)->int:
        sucursales_activas = (Sucursal.select(Sucursal.sucursal_id).where(Sucursal.activa=='S'))
        return sucursales_activas.count() 
     
         
    def getCantSucursalesConDescuentosActivos(self) ->int: 
        # Definimos la fecha actual
        fecha_actual = date.today()
    
        # Realizamos la consulta con JOIN entre Sucursal, DescuentoDetalle y DescuentoEsquema
        sucursales_con_descuentos = (Sucursal
            .select(Sucursal.sucursal_id, Sucursal.nom_sucursal)
            .join(DescuentoDetalle, on=Sucursal.sucursal_id == DescuentoDetalle.sucursal_id)
            .join(DescuentoEsquema, on=DescuentoDetalle.descuento_esquema_id == DescuentoEsquema.descuento_esquema_id)
            .where(DescuentoEsquema.fecha_vig_inicio <= fecha_actual)
            .where(DescuentoEsquema.fecha_vig_fin >= fecha_actual)
            .group_by(Sucursal.sucursal_id,Sucursal.nom_sucursal)
        ) 
        return sucursales_con_descuentos.count()  
from Models.descuento_model import DescuentoEsquema,db
from Models.sucursal_model import Sucursal
from typing import List,Optional
from apidescuentos.DAO.base_dao import BaseDAO
from DTOs.DescuentoDTO import DescuentoEsquemaDTO

from flask import request
import peewee
class DescuentoDAO(BaseDAO):
    
    def __init__(self):
        pass
    
    def get_descuentos(self)->List[DescuentoEsquema]:
        return DescuentoEsquema.select()
    
    def getDescuentoPorId(self,id_descuento):
        return DescuentoEsquema.get_or_none(DescuentoEsquema.descuento_esquema_id == id_descuento)
    
    def get_nro_descuento(self)->int:
        return db.execute_sql("SELECT nextval('descuento_esquema_descuento_esquema_id_seq');").fetchone()[0]


    def get_descuentos_paginados(self,filtros ={})->dict:
   
        query = DescuentoEsquema.select(DescuentoEsquema.descuento_esquema_id,
                                        DescuentoEsquema.nombre,    
                                        DescuentoEsquema.fecha_vig_inicio,
                                        DescuentoEsquema.fecha_vig_fin,
                                        DescuentoEsquema.tipo,
                                        DescuentoEsquema.monto_porcentaje,
                                        DescuentoEsquema.cupon,
                                        DescuentoEsquema.dias_semana,
                                        Sucursal.sucursal_id,
                                        Sucursal.nom_sucursal
                                        ).join(Sucursal,peewee.JOIN.LEFT_OUTER)
        
        for campo,fieldValue in filtros.items():
            fieldName = getattr(DescuentoEsquema,campo)
            # Si no existe la clave tipo o sea igual filtramos por where simple    
            if fieldValue['tipo'] =='=' or not('tipo' in fieldValue):
                query =query.where(fieldName == fieldValue['valor']) 
                 
            else:
                query = query.where(fieldName.contains(fieldValue['valor']))    
                    
        query = query.order_by(DescuentoEsquema.fecha_vig_inicio)  # Seleccionamos las sucursales y los ordenamos por nro de sucursal
        
        
        return DescuentoDAO.paginated(query, DescuentoEsquemaDTO)
         
    def registrarEsquemaDescuento(self,esquemaDesc):
        unDescuento = DescuentoEsquema()
        unDescuento.descuento_esquema_id = self.get_nro_descuento()
        unDescuento.nombre = esquemaDesc['nombre']
        unDescuento.fecha_vig_inicio = esquemaDesc['fecha_vig_inicio']
        unDescuento.fecha_vig_fin = esquemaDesc['fecha_vig_fin']
        unDescuento.tipo = esquemaDesc['tipo']
        unDescuento.monto_porcentaje = esquemaDesc['monto_porcentaje']
        unDescuento.sucursal_id = esquemaDesc['sucursal_id']
        unDescuento.dias_semana = esquemaDesc['dias_semana']
        unDescuento.cupon = esquemaDesc['cupon']
        unDescuento.save()
        return unDescuento
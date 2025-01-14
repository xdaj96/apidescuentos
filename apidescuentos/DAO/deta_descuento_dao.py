from Models.descuento_model import DescuentoEsquema
from Models.detadescuento_model import DescuentoDetalle
from Models.plan_os_model import PlanOS
from Models.sucursal_model import Sucursal
from Models.producto_model import Producto
from typing import List,Optional
from apidescuentos.DAO.base_dao import BaseDAO
from DTOs.DescuentoDTO import DescuentoEsquemaDTO
from flask import request
import peewee
class DetaDescuentoDAO(BaseDAO):
    
    def __init__(self):
        pass
    
    def get_descuentos(self)->List[DescuentoEsquema]:
        return DescuentoEsquema.select()
    
    def getDetalleDescuentoPorEsquema(self,id_descuento):
         # Subconsulta (equivalente al CTE)
         
        # Consulta principal
        query = (DescuentoDetalle
         .select(
             DescuentoDetalle.descuento_detalle_id,
             DescuentoDetalle.cod_rubro,
             DescuentoDetalle.cod_laboratorio,
             DescuentoDetalle.sucursal_id,
             DescuentoDetalle.cod_planos,
             DescuentoDetalle.repeticion,
             DescuentoDetalle.porcentaje_descuento,
             DescuentoDetalle.cod_alfabeta,
             Producto.cod_alfabeta,
             Producto.nro_troquel,
             Producto.cod_barraspri,
             Producto.nom_largo,
             PlanOS.cod_planos,  # Referencia a la subconsulta (CTE)
             PlanOS.nom_planos   # Referencia a la subconsulta (CTE)
         )
         .join(Producto, on=(DescuentoDetalle.cod_alfabeta == Producto.cod_alfabeta))  # JOIN con Producto
         .join(PlanOS, peewee.JOIN.LEFT_OUTER,on=(DescuentoDetalle.cod_planos == PlanOS.cod_planos),)  # JOIN con la subconsulta (CTE)
         .where(DescuentoDetalle.descuento_esquema_id == id_descuento))  # Filtro adicional

        return query
    
    def registrarLineaDescuento(self,lineaDescuento):
        """
        Registra una nueva linea de descuentos. 
        Atención: Se debe generar el Id de la linea antes de ejecutar este método
        
        Args:
            lineaDescuento (LineaDescuento): Diccionario con los  datos que se deben insertar
        """
        unaLineaDescuento = DescuentoDetalle()
        unaLineaDescuento.descuento_esquema_id = lineaDescuento['descuento_esquema_id']
        unaLineaDescuento.descuento_detalle_id = lineaDescuento['descuento_detalle_id']
        unaLineaDescuento.cod_planos = lineaDescuento['descuento_esquema_id']
        unaLineaDescuento.cod_laboratorio = lineaDescuento['descuento_esquema_id']
        unaLineaDescuento.cod_rubro = lineaDescuento['descuento_esquema_id']
        unaLineaDescuento.cod_alfabeta = lineaDescuento['cod_alfabeta']
        unaLineaDescuento.porcentaje_descuento = lineaDescuento['porcentaje_descuento']
        unaLineaDescuento.tipo = lineaDescuento['tipo']
        unaLineaDescuento.importe_fijo = lineaDescuento['importe_fijo']    
        unaLineaDescuento.save()
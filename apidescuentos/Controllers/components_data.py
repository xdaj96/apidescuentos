from DAO.descuento_dao import DescuentoDAO
from DAO.ventadiaria_os_dao import VentaDiariaOSDAO
from DAO.sucursal_dao import SucursalDAO
from DAO.productos_dao import ProductoDAO
from flask import request,Blueprint
from utils.response import apiresponse
from typing import List,Optional
from libs.JWT import token_requerido
from validations.validar_descuentos import DescuentoValidationEsquema
from marshmallow import ValidationError

#-- DAOS DE LAS ENTIDADES -----------#
DAODescuento = DescuentoDAO() 
DAOVentasOS = VentaDiariaOSDAO()
DAOSucursal = SucursalDAO()
DAOProducto = ProductoDAO()


componentsdata_controller = Blueprint('components_data',__name__)

@componentsdata_controller.route('/api/components_data/estadistica_ofertas')
@token_requerido
def get_estadistica_ofertas(current_user):
    return apiresponse(status=True,data={
        "ofertas_activas": DAODescuento.get_cant_descuentos_vigentes(),
        "ofertas_inactivas": DAODescuento.get_cant_descuentos_inactivos()
    })    


@componentsdata_controller.route('/api/components_data/estadistica_trimestral_ofertas')
@token_requerido
def get_info_trimestral_ofertas(current_user):
    total_desc_hoy = DAOVentasOS.get_total_descuentos_actual()
    return apiresponse(status=True,data={
        "descuentos_hoy":  total_desc_hoy if not(total_desc_hoy is None) else 0 ,
        "total_descuentos": DAOVentasOS.get_total_descuentos_trimestral()
    })    
 
@componentsdata_controller.route('/api/components_data/estadistica_trimestral_descuentos')
@token_requerido
def get_estadistica_trimestral_ofertas(current_user):
    desc_semestral = DAOVentasOS.get_estadistica_semestral_descuentos()
    return apiresponse(status=True,data= [descuento.to_dict() for descuento in desc_semestral])    
 

@componentsdata_controller.route('/api/components_data/sucursales_con_descuentos')
@token_requerido
def get_sucursales_con_descuentos(current_user):
    desc_semestral = DAOVentasOS.get_estadistica_semestral_descuentos()
    return apiresponse(status=True,data={"sucursales_con_descuento":DAOSucursal.getCantSucursalesConDescuentosActivos(),
                                         "total_sucursales":DAOSucursal.getCantidadSucursalesActivas()})    
 
@componentsdata_controller.route('/api/components_data/productos_con_descuento')
@token_requerido
def get_productos_en_descuento(current_user):
    productosConDescuento = DAOProducto.getCantProductosConDescuento()
    
    return apiresponse(status=True,data={"productos_con_descuento":productosConDescuento,
                                         "total_productos":0})    
 
    
        
    
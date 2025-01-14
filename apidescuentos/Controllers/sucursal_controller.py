from DAO.sucursal_dao import SucursalDAO
from flask import request,Blueprint
from utils.response import apiresponse
from typing import List,Optional
from libs.JWT import token_requerido
DAOSucursal = SucursalDAO()

sucursal_controller = Blueprint('sucursal',__name__)

@sucursal_controller.route('/api/sucursales',methods=['GET'])
@token_requerido
def listar_sucursales(current_user) ->List[dict]:
    """ 
    Retorna la lista de los usuarios 
        
    Returns:
        List[dict]: datos de los usuarios 
    """
    # definimos los parametros de consulta 
    req_data = request.args.to_dict()
    filtros = {}
    
    #si el usuario usa el search 
    if 'q' in req_data:
        if isinstance(req_data['q'],int):
            if req_data['q'] < 999:
                filtros['nro_sucursal'] = {"valor":req_data['q'],"tipo":"="}
    
        else: 
            filtros['nom_sucursal'] = {"valor":req_data['q'],"tipo":"LIKE"}
    

    # Si el usuario filtra por numero de sucursal 
    if 'nro_sucursal' in req_data: 
        if isinstance(req_data['nro_sucursal'],int):
            if req_data['nro_sucursal'] < 999:
                filtros['nro_sucursal'] = {"valor":req_data['nro_sucursal'],"tipo":"="}
    
    # Si el usuario filtra por cuit
    if 'cuit' in req_data: 
        if isinstance(req_data['cuit'],str):
            filtros['cuit'] = {"valor":req_data['cuit'],"tipo":"="}
    
    
    # Si el usuario filtra por razon social
    if 'razon_social' in req_data: 
        if isinstance(req_data['razon_social'],str):
            filtros['razon_social'] = {"valor":req_data['razon_social'],"tipo":"LIKE"}
    
    
    # Si el usuario filtra por  sucursales activas    
    if 'activa' in req_data: 
        if isinstance(req_data['activa'],str):
                    filtros['activa'] = {"valor":req_data['activa'],"tipo":"="}
    
    lista_sucursales = DAOSucursal.get_sucursales_paginadas(filtros= filtros)
    return  apiresponse(True,data = lista_sucursales)
    

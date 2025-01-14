from DAO.planes_os_dao import PlanesOSDAO 
from flask import request,Blueprint
from utils.response import apiresponse
from typing import List,Optional
from libs.JWT import token_requerido
 
DAOPlanesOS = PlanesOSDAO()
planes_os_controller = Blueprint('planes_os',__name__)

@planes_os_controller.route('/api/planes_os',methods=['GET'])
@token_requerido
def listar_planes(current_user):
    """ 
    Retorna la lista de los planes de coseguro o obrasocial 
        
    Returns:
        List[dict]: datos de los planes 
    """
    # definimos los parametros de consulta 
    req_data = request.args.to_dict()
    filtros = {}
    
    #si el usuario usa el search 
    if 'q' in req_data:
            filtros['search'] = {"valor":req_data['q'],"tipo":"LIKE"}
     
    # Si el usuario filtra por numero de sucursal 
    if 'cod_planos' in req_data: 
        filtros['cod_planos'] = {"valor":req_data['cod_planos'],"tipo":"="}
    
  
    lista_descuentos = DAOPlanesOS.get_planes_paginados(filtros= filtros)
    return  apiresponse(True,data = lista_descuentos)
from DAO.rubros_dao import RubroDAO 
from flask import request,Blueprint
from utils.response import apiresponse
from typing import List,Optional
from libs.JWT import token_requerido
 
DAORubro = RubroDAO()
rubro_controller = Blueprint('rubro',__name__)

@rubro_controller.route('/api/rubros',methods=['GET'])
@token_requerido
def listar_rubros(current_user):
    """ 
    Retorna la lista de los rubros 
        
    Returns:
        List[dict]: datos paginados de los rubros 
    """
    # definimos los parametros de consulta 
    req_data = request.args.to_dict()
    filtros = {}
    
    #si el usuario usa el search 
    if 'q' in req_data:
            filtros['search'] = {"valor":req_data['q'],"tipo":"LIKE"}
     
    # Si el usuario filtra por numero de sucursal 
    if 'cod_rubro' in req_data: 
        filtros['cod_rubro'] = {"valor":req_data['cod_rubro'],"tipo":"="}
    
  
    lista_rubros = DAORubro.get_rubros_paginados(filtros= filtros)
    return  apiresponse(True,data = lista_rubros)
from DAO.laboratorio_dao import LaboratorioDAO
from flask import request,Blueprint
from utils.response import apiresponse
from typing import List,Optional
from libs.JWT import token_requerido
DAOLaboratorio = LaboratorioDAO()
laboratorios_controller = Blueprint('laboratorios',__name__)

@laboratorios_controller.route('/api/laboratorios',methods=['GET'])
@token_requerido
def listar_laboratorios(current_user) ->List[dict]:
    """ 
    Lista todos los laboratorios paginados
        
    Returns:
        List[dict]: datos de los usuarios 
    """
    # definimos los parametros de consulta 
    req_data = request.args.to_dict()
    filtros = {}
    
    #si el usuario usa el search 
    if 'q' in req_data:
            filtros['nom_laboratorio'] = {"valor":req_data['q'],"tipo":"LIKE"}
    

    # Si el usuario filtra por numero de sucursal 
    if 'cod_laboratorio' in req_data: 
                filtros['cod_laboratorio'] = {"valor":req_data['cod_laboratorio'],"tipo":"="}
    
  
    lista_laboratorios = DAOLaboratorio.get_laboratorios(filtros= filtros)
    return  apiresponse(True,data = lista_laboratorios)
   
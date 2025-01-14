from DAO.usuario_dao import UsuarioDAO
from flask import request,Blueprint
from utils.response import apiresponse
from typing import List,Optional
from libs.JWT import token_requerido
DAO = UsuarioDAO()

usuario_controller = Blueprint('usuarios',__name__)

@usuario_controller.route('/api/usuarios',methods=['GET'])
@token_requerido
def listarUsuarios(current_user) ->List[dict]:
    """ 
    Retorna la lista de los usuarios 
        
    Returns:
        List[dict]: datos de los usuarios 
    """
    usuarios = DAO.get_usuarios_paginados()
    return  apiresponse(True,data = usuarios)
    

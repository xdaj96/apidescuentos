from flask import Blueprint,request
from utils.response import apiresponse 
from DAO.usuario_dao import UsuarioDAO
from typing import List,Optional 
from libs.JWT import generar_token
auth_controller = Blueprint('auth',__name__)
usuarioDAO = UsuarioDAO()
@auth_controller.route('/api/auth/login',methods=['POST'])

def login() ->List[dict]:
    """ 
    Metodo que devuelve el usuario registrado
    Returns:
        List[dict]: Datos del usuario
    """
    data = request.get_json()
    unUsuario = usuarioDAO.login(data['email'],data['password'])
    
    
    if unUsuario is not None : 
        
        # Verificamos que el usuario cuente con acceso total 
        
        if unUsuario.tieneAccesoTotal(): 
            userdata = {
                "user":unUsuario.to_dict(),
                "token": generar_token(unUsuario.usuario_id)
            }
            return apiresponse(True,data = userdata)
        else: 
            return apiresponse(False,'El usuario no tiene permiso para acceder al sistema',data = {})        
    else: 
        return apiresponse(False,'El usuario no existe',data = {})
    
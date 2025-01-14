from Models.usuario_model import Usuario
from typing import List,Optional
from apidescuentos.DAO.base_dao import BaseDAO
from DTOs.UsuarioDTO import UsuarioDTO
import peewee
class UsuarioDAO(BaseDAO):
    
    def __init__(self):
        pass
    
    def get_usuarios(self)->List[Usuario]:
        return Usuario.select()
    
    
    def get_usuarios_paginados(self,page = 1,per_page = 20)->dict:
   
        query = Usuario.select().order_by(Usuario.apellido)  # Seleccionamos los usuarios y los ordenamos por apellido
        return UsuarioDAO.paginated(query=query,dtoclass= UsuarioDTO)
         
   
    def getUsuarioPorId(self,id_usuario)->Optional[Usuario]:
        return Usuario.get_by_id(id_usuario)
    
    
    # Valida si el email ya esta registrado 
    def existeEmail(self,emailreq)->bool:
        unUsuario = Usuario.get_or_none(Usuario.email == emailreq)
        if unUsuario == None:
            return False
        else: 
            return True
    
    # Valida si el usuario ya esta registrado 
    def existeUsuario(self,usuarioReq)->bool:
        unUsuario = Usuario.get_or_none(Usuario.nombre_usuario == usuarioReq)
        if unUsuario == None:
            return False
        else: 
            return True
    

    # Agrega el usuario a la base de datos      
    def agregarUsuario(self,usuario:Usuario) ->bool:
        return Usuario.save()
        
    
    # Realiza el proceso de login de usuario 
     
    def login(self,nombre_usuario:str,password: str) ->Optional[Usuario]:
        query = Usuario.select()
        if nombre_usuario:
            query = query.where(Usuario.nombre_usuario == (nombre_usuario))  # Filtro por nombre
        if password and query is not None:
            query = query.where(Usuario.password == (password))  # Filtro por email

        if query.count() >0:
            return query.first()
        return None
    
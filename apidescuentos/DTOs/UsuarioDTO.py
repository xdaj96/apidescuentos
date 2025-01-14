from Models.usuario_model import Usuario
class UsuarioDTO: 
    
    def __init__(self,id_usuario,nombre,apellido,acceso_total,email,usuario):
        self.usuario_id = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.acceso_total = acceso_total
        self.email = email
        self.usuario = usuario
    
    def nombreCompleto(self):
        return self.nombre + ' ' + self.apellido
    
    @classmethod
    def from_model(cls,model:Usuario):
        return cls(model.usuario_id,model.nombre,model.apellido,model.acceso_total,model.email,model.nombre_usuario)
    
    
    def to_dict(self):
        return {
            'id_usuario':self.usuario_id,
            'nombre': self.nombreCompleto(),
            'acceso_total': self.acceso_total,
            'email': self.email,
            'usuario': self.usuario
            
        }
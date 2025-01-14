from Models.sucursal_model import Sucursal
class SucursalDTO: 
    
    def __init__(self,sucursal_id,nom_sucursal,nro_sucursal,razon_social,cuit,direccion,ciudad,provincia,activa):
        self.sucursal_id = sucursal_id
        self.nom_sucursal = nom_sucursal
        self.nro_sucursal = nro_sucursal
        self.razon_social = razon_social
        self.cuit = cuit
        self.direccion = direccion
        self.ciudad = ciudad
        self.provincia = provincia
        self.activa = activa
    
    def nombreCompleto(self):
        return self.nombre + ' ' + self.apellido
    
    @classmethod
    def from_model(cls,model:Sucursal):
        return cls(
            model.sucursal_id,
            model.nom_sucursal,
            model.nro_sucursal,
            model.razon_social,
            model.cuit,
            model.direccion,
            model.ciudad,
            model.provincia,
            model.activa   
        )
    
    def to_dict(self):
        return {
            "sucursal_id": self.sucursal_id,
            "nom_sucursal": self.nom_sucursal,
            "nro_sucursal":self.nro_sucursal,
            "razon_social":self.razon_social,
            "cuit": self.cuit,
            "direccion": self.direccion,
            "ciudad": self.ciudad,
            "provincia": self.provincia,
            "activa": self.activa 
        }
         
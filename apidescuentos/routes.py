from flask import Flask

from Controllers.usuario_controller import usuario_controller
from Controllers.auth_controller import auth_controller
from Controllers.sucursal_controller import sucursal_controller 
from Controllers.descuento_Controller import descuento_controller
from Controllers.planes_os_controller import planes_os_controller
from Controllers.productos_controller import productos_controller
from Controllers.rubro_controller import rubro_controller
controladores = [
    usuario_controller,
    auth_controller,
    sucursal_controller,
    descuento_controller,
    planes_os_controller,
    productos_controller,
    rubro_controller
] 
 
 
 
def initialize_routes(app:Flask):
    # Registrar el controlador de usuarios
    for controlador in controladores:
        app.register_blueprint(controlador) 
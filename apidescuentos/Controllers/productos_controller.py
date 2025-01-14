from DAO.productos_dao import ProductoDAO 
from flask import request,Blueprint
from utils.response import apiresponse
from typing import List,Optional
from libs.JWT import token_requerido
 
DAOProductos = ProductoDAO()
productos_controller = Blueprint('productos',__name__)

@productos_controller.route('/api/productos',methods=['GET'])
@token_requerido
def listar_productos(current_user):
    """ 
    Retorna la lista de los productos 
        
    Returns:
        List[dict]: datos de los productos 
    """
    # definimos los parametros de consulta 
    req_data = request.args.to_dict()
    filtros = {}
    query_value = "" 

    # Si el usuario usa el 'search'
    if 'q' in req_data:
        query_value = req_data['q']
        print(query_value)

        # Verificar si el valor es un número con 13 dígitos (posible código de barras)
        if query_value.isdigit() and len(query_value) == 13:
            filtros['cod_barraspri'] = {"valor": query_value, "tipo": "="}

        # Verificar si el valor es un número con entre 4 y 12 dígitos (posible número de troquel)
        elif query_value.isdigit() and 4 <= len(query_value) < 13:
            filtros['nro_troquel'] = {"valor": query_value, "tipo": "="}

        # Si no es un número, es una búsqueda general
    else:
        filtros['search'] = {"valor": query_value, "tipo": "LIKE"}

        # Si el usuario filtra por 'nro_troquel'
        if 'nro_troquel' in req_data:
            filtros['nro_troquel'] = {"valor": req_data['nro_troquel'], "tipo": "="}

        # Si el usuario filtra por 'c_barras'
        if 'c_barras' in req_data:
            filtros['cod_barraspri'] = {"valor": req_data['c_barras'], "tipo": "="}

        # Ejecutar la consulta con los filtros aplicados
    
    lista_descuentos = DAOProductos.get_productos_paginados(filtros= filtros)
    return  apiresponse(True,data = lista_descuentos)
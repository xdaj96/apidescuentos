from flask import jsonify,request

def apiresponse(status, message: str = 'La peticion se completo correctamente', data: dict = None,status_code = 200):
    """
    Crea una respuesta API estándar con formato JSON.

    :param status_code: Código de estado HTTP para la respuesta.
    :param message: Mensaje para incluir en la respuesta.
    :param data: Datos adicionales a incluir en la respuesta (opcional).
    :return: Respuesta JSON con el código de estado y el mensaje.
    """
    # Si son datos paginados mostramos un tipo de respuesta 
    
    if 'token' in data:
        response = {
            "token":data['token'],
            "data":data['user']
        }
    elif ('results' in data) and ( 'total_pages' in data):
        
        page = request.args.get('page',1)
        
        response = {
            "status":status,
            "data": data['results'], 
            "total_records": data['total_records'],
            "current_page": data['current_page'],
            "total":data['total_pages'],
            "perPage":data['per_page'],
            "page":page
        }
    else: 
        response = {
            "status":status,
            "message": message,
            "data": data or {}
        }
    return jsonify(response), status_code
import jwt
import datetime
import os
from dotenv import load_dotenv
from flask import request,jsonify
from functools import wraps
from DAO.usuario_dao import UsuarioDAO


# Cargar las variables de entorno
load_dotenv()

# Obtener la clave secreta desde las variables de entorno
SECRET_KEY = os.getenv('SECRET_KEY')
JWT_EXPIRATION_DELTA = int(os.getenv('JWT_EXPIRATION_DELTA'))

# Función para generar un token JWT
def generar_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=JWT_EXPIRATION_DELTA)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

# Función para verificar el token JWT
def verificar_token(token):
    try:
        # Decodificar el token con la clave secreta
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None  # El token ha expirado
    except jwt.InvalidTokenError:
        return None  # Token inválido

# Decorador para proteger rutas con JWT
def token_requerido(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        # Obtener el token del encabezado Authorization
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token faltante'}), 403
        
        # El token debe tener el formato "Bearer <token>"
        token = token.split(" ")[1]

        # Verificar el token
        payload = verificar_token(token)
        
        if payload is None:
            return jsonify({'message': 'Token inválido o expirado'}), 401
        
        # Si el token es válido, pasamos el user_id al endpoint
        usuarioDAO = UsuarioDAO()
        current_user = usuarioDAO.getUsuarioPorId(payload['user_id']).to_dict()
        
        
        
        return f(*args, **kwargs, current_user=current_user)

    return decorator
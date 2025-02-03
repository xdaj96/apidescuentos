from DAO.descuento_dao import DescuentoDAO
from DAO.deta_descuento_dao import DetaDescuentoDAO
from flask import request,Blueprint
from utils.response import apiresponse
from typing import List,Optional
from libs.JWT import token_requerido
from validations.validar_descuentos import DescuentoValidationEsquema
from marshmallow import ValidationError
DAODescuento = DescuentoDAO()
DAODetaDescuento = DetaDescuentoDAO()
descuentoValidacion = DescuentoValidationEsquema()
descuento_controller = Blueprint('descuentos',__name__)

@descuento_controller.route('/api/descuentos',methods=['GET'])
@token_requerido
def listar_descuentos(current_user) ->List[dict]:
    """ 
    Retorna la lista de los usuarios 
        
    Returns:
        List[dict]: datos de los usuarios 
    """
    # definimos los parametros de consulta 
    req_data = request.args.to_dict()
    filtros = {}
    
    #si el usuario usa el search 
    if 'q' in req_data:
            filtros['nom_sucursal'] = {"valor":req_data['q'],"tipo":"LIKE"}
    

    # Si el usuario filtra por numero de sucursal 
    if 'sucursal_id' in req_data: 
                filtros['sucursal_id'] = {"valor":req_data['sucursal_id'],"tipo":"="}
    
  
    lista_descuentos = DAODescuento.get_descuentos_paginados(filtros= filtros)
    return  apiresponse(True,data = lista_descuentos)
    
@descuento_controller.route('/api/descuentos/ver/<int:descuento_esquema_id>', methods=['GET'])
@token_requerido
def ver_descuento( descuento_esquema_id,current_user):
    
    unDescuento = DAODescuento.getDescuentoPorId(descuento_esquema_id).to_dict()
    
    if unDescuento is not None:
        unDescuento['detalle'] = [item.to_dict() for item in DAODetaDescuento.getDetalleDescuentoPorEsquema(descuento_esquema_id)]
    
    
    return apiresponse(status=True,data=unDescuento)

@descuento_controller.route('/api/descuentos',methods=['POST'])
@token_requerido
def registrar_descuento(current_user):
    data = request.get_json()
    try:
        # Validamos si los datos ingresados corresponden a un descuento
        descuentoValidacion.load(data)
        
        # Registramos el descuento en la base de datos
        DAODescuento.iniciarTransaccion()
        unDescuento = DAODescuento.registrarEsquemaDescuento(esquemaDesc=data)
        dictDescuento = unDescuento.to_dict()
        detalle = []
        print(data)
        # Registramos el detalle del descuento 
        for renglon in data['detalle']:
          
            renglon['descuento_esquema_id'] = dictDescuento['descuento_esquema_id']  
            renglon['porcentaje_descuento'] = dictDescuento['monto_porcentaje']
             

            detalle.append(DAODetaDescuento.registrarLineaDescuento(renglon))    
      
        DAODescuento.commit()
        dictDescuento['detalle'] = [unRenglon.to_dict() for unRenglon in detalle]    
        
        return apiresponse(True,'El descuento se registro correctamente',dictDescuento)     
        
        
    except ValidationError as err:
        return apiresponse(False,err.messages,[],500)
   
    except Exception as e:
        DAODescuento.rollback()
        print(e)
        return apiresponse(False,'La peticion no se pudo completar',[],500)
    
@descuento_controller.route('/api/descuentos/<int:descuento_esquema_id>',methods=['DELETE'])
@token_requerido
def eliminar_descuento(descuento_esquema_id,current_user):
    unDescuento = DAODescuento.getDescuentoPorId(descuento_esquema_id).to_dict()
    
    if unDescuento is None: 
        return apiresponse(status=False,data={},message='El descuento no existe')
     
    if DAODescuento.eliminar_descuento(descuento_esquema_id):
        return apiresponse(status=True,data=unDescuento,message='El descuento se elimino correctamente')

    return apiresponse(status=False,data=unDescuento,message='no se pudo eliminar el descuento')

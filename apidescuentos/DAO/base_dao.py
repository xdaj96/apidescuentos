import peewee
from playhouse.shortcuts import model_to_dict
from DTOs.BaseDTO import BaseDTO
from libs.Paginator import Paginator
from flask import request
from database import db
class BaseDAO():
    
    def __init__(self):
        pass
    
    def paginated(query: peewee.SelectQuery,dtoclass):
       return Paginator(query,dtoclass).paginate()   
   
    def iniciarTransaccion(self):
        return db.begin()
    
    def commit(self):
        return db.commit()
    
    def rollback(self):
        return db.rollback()
    
    def registrosAfectados(self):
        return db.rows_affected()    
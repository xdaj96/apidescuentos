from DTOs.BaseDTO import BaseDTO
from flask import request

class Paginator:
    def __init__(self, query, dto_class, page=1, per_page=20):
        self.query = query
        self.dto_class = dto_class or BaseDTO  # Aquí pasamos el DTO dinámicamente
        self.page = int(request.args.get('page', 1))  # Página por defecto es 1
        self.per_page = int(request.args.get('limit', 20))  # Resultados por página por defecto 20


    def paginate(self):
        # Calcular el desplazamiento (offset)
        offset = (self.page - 1) * self.per_page

        # Realizar la consulta con paginación
        paginated_query = self.query.limit(self.per_page).offset(offset)

     

        
        # Obtener los resultados y convertirlos en DTOs usando la clase DTO pasada
         

        # Obtener el total de registros
        total_records = self.query.count()
        # Calcular el número total de páginas
        total_pages = (total_records // self.per_page) + (1 if total_records % self.per_page > 0 else 0)


        # Devolver los resultados junto con el total de registros y las páginas
        return {
            'results': [item.to_dict() for item in paginated_query],
            'total_records': total_records,
            'total_pages': total_pages,
            'current_page': self.page,
            'per_page': self.per_page
        }
        
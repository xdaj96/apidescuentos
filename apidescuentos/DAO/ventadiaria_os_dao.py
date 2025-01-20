from Models.ventas_os_model import VentasOS,dbAutodw 
from typing import List,Optional
from apidescuentos.DAO.base_dao import BaseDAO
from DTOs.rubro_dto import RubroDTO
from DTOs.estadistica_desc_dto import EstadisticaDescDto
from peewee import fn
from dateutil.relativedelta import relativedelta

from datetime import datetime

# Diccionario para mapear números de mes a nombres abreviados en español
meses_abreviados = {
    1: 'Ene', 2: 'Feb', 3: 'Mar', 4: 'Abr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Ago', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dic'
}

class VentaDiariaOSDAO(BaseDAO):
    
    
    def get_total_descuentos_actual(self)->float:
        """
        Devuelve el total de descuentos de la fecha actual
        Returns:
            float: Total de descuentos en pesos
            
        """ 
        fecha_actual = datetime.now()
        return VentasOS.select(fn.SUM(VentasOS.importe_desc)).where(
              (VentasOS.fecha.between(fecha_actual,fecha_actual))&
            (VentasOS.cod_planos == 'ZWA')
        ).scalar()
    
    def get_total_descuentos_trimestral(self)->float:
        """ 
        Devuelve el total de descuentos trimestral    
        Returns:
            float: Total de descuentos en pesos
        """
        fecha_actual = datetime.now()
        fecha_anterior = fecha_actual - relativedelta(months=3)

        return VentasOS.select(fn.SUM(VentasOS.importe_desc)).where(
            (VentasOS.fecha.between(fecha_anterior,fecha_actual))&
            (VentasOS.cod_planos == 'ZWA')
        ).scalar()
    
    def get_estadistica_semestral_descuentos(self):
        mesesdesc = [] 
        fecha_actual = datetime.now()
        fecha_anterior = fecha_actual - relativedelta(months=6)
        # Agrupar por año y mes, y sumar 'importe_desc'
        query = (VentasOS
         .select(VentasOS.fecha.year.alias('anio'),
                 VentasOS.fecha.month.alias('mes'),
                 fn.SUM(VentasOS.importe_desc).alias('total_importe_desc'))
         .where(VentasOS.fecha.between(fecha_anterior,fecha_actual) &  (VentasOS.cod_planos == 'ZWA'))
         .group_by(VentasOS.fecha.year,VentasOS.fecha.month)
         .order_by(VentasOS.fecha.year,
                   VentasOS.fecha.month))
        print(query.sql())
# Ejecutar y mostrar los resultados con el formato 'Mes-Año'
        for row in query:
            mes_nombre = meses_abreviados[int(row.mes)]  # Obtener el nombre del mes
            mesesdesc.append(EstadisticaDescDto(mes_nombre+' '+str(row.anio),row.total_importe_desc))
        return mesesdesc
from Models.ventas_os_model import VentasOS,dbAutodw 
from Models.venta_diaria_model import VentaDiaria
from Models.descuento_model import DescuentoEsquema
from Models.detadescuento_model import DescuentoDetalle
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
        fecha_anterior = fecha_actual - relativedelta(days=1)


        query = (VentaDiaria.select(fn.SUM(VentaDiaria.venta_pesos)).join(DescuentoDetalle, on=(VentaDiaria.cod_alfabeta == DescuentoDetalle.cod_alfabeta))
              .join(DescuentoEsquema, on=(
                  (DescuentoDetalle.descuento_esquema_id == DescuentoEsquema.descuento_esquema_id) &
                  (DescuentoEsquema.sucursal_id == VentaDiaria.sucursal_id) &
                  (VentaDiaria.fecha.between(DescuentoEsquema.fecha_vig_inicio, DescuentoEsquema.fecha_vig_fin))
              ))
              .where(VentaDiaria.fecha.between(fecha_anterior,fecha_actual)).scalar())
         
        return  query
    
    def get_total_descuentos_trimestral(self)->float:
        """ 
        Devuelve el total de descuentos trimestral    
        Returns:
            float: Total de descuentos en pesos
        """
        fecha_actual = datetime.now()
        fecha_anterior = fecha_actual - relativedelta(months=3)
        print(
            VentaDiaria.select(fn.SUM(VentaDiaria.venta_pesos)).join(DescuentoDetalle, on=(VentaDiaria.cod_alfabeta == DescuentoDetalle.cod_alfabeta))
              .join(DescuentoEsquema, on=(
                  (DescuentoDetalle.descuento_esquema_id == DescuentoEsquema.descuento_esquema_id) &
                  (DescuentoEsquema.sucursal_id == VentaDiaria.sucursal_id) &
                  (VentaDiaria.fecha.between(DescuentoEsquema.fecha_vig_inicio, DescuentoEsquema.fecha_vig_fin))
              ))
              .where(VentaDiaria.fecha.between(fecha_anterior,fecha_actual)).sql()
        )

        return (VentaDiaria.select(fn.SUM(VentaDiaria.venta_pesos)).join(DescuentoDetalle, on=(VentaDiaria.cod_alfabeta == DescuentoDetalle.cod_alfabeta))
              .join(DescuentoEsquema, on=(
                  (DescuentoDetalle.descuento_esquema_id == DescuentoEsquema.descuento_esquema_id) &
                  (DescuentoEsquema.sucursal_id == VentaDiaria.sucursal_id) &
                  (VentaDiaria.fecha.between(DescuentoEsquema.fecha_vig_inicio, DescuentoEsquema.fecha_vig_fin))
              ))
              .where(VentaDiaria.fecha.between(fecha_anterior,fecha_actual))
        ).scalar()
    
    def get_estadistica_semestral_descuentos(self):
        mesesdesc = [] 
        fecha_actual = datetime.now()
        fecha_anterior = fecha_actual - relativedelta(months=4)
        # Agrupar por año y mes, y sumar 'importe_desc'
        query =(VentaDiaria 
               .select(VentaDiaria.fecha.year.alias('anio'),
                 VentaDiaria.fecha.month.alias('mes'),
                 fn.SUM(VentaDiaria.venta_pesos).alias('total_importe_desc'))
              .join(DescuentoDetalle, on=(VentaDiaria.cod_alfabeta == DescuentoDetalle.cod_alfabeta))
              .join(DescuentoEsquema, on=(
                  (DescuentoDetalle.descuento_esquema_id == DescuentoEsquema.descuento_esquema_id) &
                  (DescuentoEsquema.sucursal_id == VentaDiaria.sucursal_id) &
                  (VentaDiaria.fecha.between(DescuentoEsquema.fecha_vig_inicio, DescuentoEsquema.fecha_vig_fin))
              ))
              .where(VentaDiaria.fecha.between(fecha_anterior,fecha_actual)).group_by(VentaDiaria.fecha.year,VentaDiaria.fecha.month)
         .order_by(VentaDiaria.fecha.year,
                   VentaDiaria.fecha.month))
       
       
# Ejecutar y mostrar los resultados con el formato 'Mes-Año'
        for row in query:
            mes_nombre = meses_abreviados[int(row.mes)]  # Obtener el nombre del mes
            mesesdesc.append(EstadisticaDescDto(mes_nombre+' '+str(row.anio),row.total_importe_desc))
        return mesesdesc
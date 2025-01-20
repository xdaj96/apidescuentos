
class EstadisticaDescDto:
    
    def __init__(self,mes,total_descuento):
        self.label = mes
        self.value = total_descuento
        
    def to_dict(self):
        return {
            "mes":self.label,
            "total_venta":self.value
        }
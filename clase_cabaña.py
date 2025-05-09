class Cabania:
    __nro_cabania:int
    __cant_habitaciones:int
    __cant_camas_gran:int
    __cant_camas_chic:int
    __importe_dia:float

    def __init__(self):
        self.__nro_cabania = 0
        self.__cant_habitaciones = 0
        self.__cant_camas_gran = 0
        self.__cant_camas_chic = 0
        self.__importe_dia = 0.0

    def get_nro_cabania(self):
        return self.__nro_cabania
    def get_cantidad_habitaciones(self):
        return self.__cant_habitaciones
    def get_cantidad_camas_grandes(self):
        return self.__cant_camas_gran
    def get_cantidad_camas_chicas(self):
        return self.__cant_camas_chic
    def get_importe_dia(self):
        return self.__importe_dia
    def __mul__(self,otro):
        resul1 = otro.get_cantidad_camas_grandes() * 2
        return resul1
    def __add__(self,aux_resul):
        return aux_resul + self.get_cantidad_camas_chicas()
    def __ge__(self,otro):
        return self.__cant_habitaciones >= otro.get_cantidad_habitaciones()
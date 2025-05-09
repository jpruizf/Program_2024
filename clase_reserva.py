class Reserva:
    __nro_res:int
    __nombre_res:str
    __nro_cabania:int
    __fecha_ini:str
    __cant_huespedes:int
    __cant_dias:int
    __importe_senia:float

    def __init__(self):
        self.__nro_res = 0
        self.__nombre_res = ""
        self.__nro_cabania = 0
        self.__fecha_ini = ""
        self.__cant_huespedes = 0
        self.__cant_dias = 0
        self.__importe_senia = 0.0
    def get_nro_reserva(self):
        return self.__nombre_res
    def get_nombre_reserva(self):
        return self.__nombre_res
    def get_numero_cabania(self):
        return self.__nro_cabania
    def get_fecha_inicio(self):
        return self.__fecha_ini
    def get_cantidad_huespedes(self):
        return self.__cant_huespedes
    def get_cantidad_dias(self):
        return self.__cant_dias
    def get_senia(self):
        return self.__importe_senia
    def __lt__(self,otro):
        return self.__fecha_ini < otro.get_fecha_inicio()
    def __eq__(self,otro):
        return self.__fecha_ini == otro.get_fecha_inicio()
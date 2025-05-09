from clase_reserva import Reserva
import csv

class Gestor_Reserva:
    __listado_reservas:list
    __importe_total:float

    def __init__(self):
        self.__listado_reservas = []
        self.__importe_total = 0.0

    def agragar_reserva(self,Una_reserva):
        self.__listado_reservas.append(Una_reserva)
    
    def cargar_reserva(self):
        bandera = False
        with open('reservas.csv') as archivo_reserva:
            lector = csv.reader(archivo_reserva,delimiter=';')
            for fila in lector:
                if not bandera:
                    bandera = True
                else:
                    Una_reserva = Reserva()
                    self.agragar_reserva(Una_reserva)
        archivo_reserva.close()
    '''inciso b'''
    def __mul__(self,valor_dia:float):
        total = valor_dia * self.get_cantidad_dias()
        return total
    def __sub__(self,otro):
        self.__importe_total = otro.get_senia() - otro.get_senia()
        return self.__importe_total
    def ordenar_fechas(self):
        self.__listado_reservas.sort()
    def mostrar_listado(self,valor_dia):
        for i in range(self.__listado_reservas):
            print(i.get_numero_cabania()/i.__importe_total()/i.get_cantidad_dias()/i.get_senia()/valor_dia)
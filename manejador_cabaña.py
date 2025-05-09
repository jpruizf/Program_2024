from clase_cabaña import Cabania
import numpy as np
import csv

class Gestor_Cabania:
    __cantidad:int
    __dimension:int
    __incremento = 10
    __listado_cabanias:np.ndarray

    def __init__(self,dimension,incremento = 10):
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento
        self.__listado_cabanias = np.empty(dimension,Cabania)
    
    def agregar_cabania(self,Una_cabania):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__listado_cabanias.resize(self.__dimension)
        self.__listado_cabanias[self.__cantidad] = Una_cabania
        self.__cantidad
    
    def cargar_cabania(self):
        bandera = False
        with open('cabañas.csv') as archivo_cabanias:
            lector = csv.reader(archivo_cabanias,delimiter=';')
            for fila in lector:
                if not bandera:
                    bandera = True
                else:
                    Una_cabania = Cabania()
                    self.agregar_cabania(Una_cabania)
        archivo_cabanias.close()
    '''inciso a'''
    def buscar_canti_habitaciones(self,elemento:int):
        bandera = False
        encontrado = None
        indice = None
        while not bandera and indice < len(self.__listado_cabanias):
            if elemento >= self.__listado_cabanias[indice].get_cantidad_habitaciones():
                bandera = True
                encontrado = indice
            else:
                indice += 1
        return encontrado
    
    def mostrar_habitaciones(self,elemento):
        for elemento in range(self.__listado_cabanias):
            print(elemento.get_numero_cabania())
    
    '''inciso b'''
    def retornar_valor_x_dia(self):
        return self.get_importe_dia()
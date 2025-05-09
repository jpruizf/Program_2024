from manejador_cabaña import Gestor_Cabania
from manejador_reserva import Gestor_Reserva
def menu():
    print("Ingrese 1->inciar | 0->Terminar")
    inicio = input("Seleccione una de las opciones->")
    while inicio != '0':
        M_Cab = Gestor_Cabania(10)
        M_Res = Gestor_Reserva()
        print("a->Ver las cabañas que tienen una capacidad mayor o igual para una cantidad de huespedes")
        print("b->Ver fecha de inicio de hospedaje reservado mas el importe total para cada cabaña")
        opcion = input("Seleccione una de las opciones->")
        if opcion == 'a':
            M_Cab.cargar_cabania()
            aux = int(input("Cantidad de huespedes->"))
            valor = int(M_Cab.buscar_canti_habitaciones(aux))
            M_Cab.mostrar_habitaciones(valor)
        elif opcion == 'b':
            M_Res.cargar_reserva()
            M_Res.ordenar_fechas()
            dato = float(M_Cab.retornar_valor_x_dia())
            aux1 = M_Res.__mul__(dato)
            total = float(M_Res.__sub__(aux1))
            M_Res.mostrar_listado(dato)
        print("Ingrese 1->inciar | 0->Terminar")
        inicio = input("Seleccione una de las opciones->")

if __name__ == '__main__':
    menu()
from Cliente import *
from Poliza import *

def menu(opciones):
    for i, opcion in enumerate(opciones):
        print(f"[{i+1}. {opcion}")
    opcion = input(" Ingrese el numero de opcion que desea elegir: ")
    while not opcion.isnumeric() or not int(opcion) in range(len(opciones)+1):
        opcion=input( "Error, ingrese un numero valido")
    opcion =int(opcion)-1
    return opcion 



def menu_inicio():
    clientes =[]
    while True:
        print("Bienvenido")
        opciones_inicio =["Registrar poliza", " Ver estadisticas ","Salir" ]
        opcion_inicio = menu(opciones_inicio)
        if opcion_inicio ==0:
            crear_cliente(clientes)
            

        elif opcion_inicio ==1: 
            pass
        elif opcion_inicio ==12: 
            break





def crear_cliente(clientes):
    nombre = input(" Ingrese su nombre: ")
    apellido  = input(" Ingrese su apellido: ")
    ci  = input(" Ingrese su cedula: ")
    direccion  = input(" Ingrese su direccion: ")
    telefono  = input(" Ingrese su telefono: ")
    cliente = Cliente(nombre,apellido,ci,direccion,telefono)
    clientes.append(cliente)

    crear_poliza(cliente) 


def crear_poliza(cliente):
    edades_asegurados =[]
    while True:
        print("Registro de polizas")
        opciones_polizas = ["De Salud", "De vehiculo", " Salir"]
        tipo  =menu(opciones_polizas)
        if tipo ==0:
            tipo= " De salud"
            while True:
                monto=0
                edad_asegurado = int(input( "Ingrese la edad de su asegurado"))
                edades_asegurados.append(edad_asegurado)
                if (edad_asegurado) ==0 or (edad_asegurado)<=10:
                    monto+= 20
                elif (edad_asegurado) ==11 or (edad_asegurado)<=20:
                    monto+= 30
                elif (edad_asegurado) ==21 or (edad_asegurado)<=40:
                    monto+= 50
                elif (edad_asegurado)>=41:
                    monto+= 70

                mas_asegurados = input( "Desea agregar a otro asegurado? Si no desea agregar a nadie pulse (0) sino pulse cualquier tecla")
                if mas_asegurados =="0":
                    break
                
            counter =0
            for asegurado in edades_asegurados:
                counter+=1

            suma= counter*100000
            total = monto

            print(suma)
            print(monto)

            poliza_salud = Poliza_salud(tipo,monto," 22 de noviembre del 2023","22 de noviembre del 2024",counter,suma,total)






        elif tipo ==1: 
            tipo = " De vehiculo"
            marca = input(" Ingrese la marca de su vehiculo: ")
            modelo= input(" Ingrese el modelo de su vehiculo: ")
            año = input(" Ingrese el año de su vehiculo: ")
            placa = input(" Ingrese la placa de vehiculo: ")
            vehiculotypes = ["Moto", "Carro", "Camioneta"]
            vehiculotype1 = menu(vehiculotypes)
            if vehiculotype1 ==0:
                monto = 15

            elif vehiculotype1 ==1:
                monto = 20

            elif vehiculotype1 ==2:
                monto = 30

            vehiculotype = vehiculotypes[vehiculotype1]



            poliza_vehiculo = Poliza_Automovil(tipo,monto," 22 de noviembre del 2023","22 de noviembre del 2024",vehiculotype, marca,modelo,año,placa, total)
        
        factura(cliente,poliza_salud,poliza_vehiculo)

        

      


    
def factura(cliente,poliza_salud,poliza_vehiculo):
    cliente.show()
    poliza_salud.show()
    poliza_vehiculo.show()


def estadisticas(clientes):
    pass




        
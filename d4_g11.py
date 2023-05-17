

# Usamos el modulo del sistema para borrar la consola luego de cada interaccion
import os
 


# Creamos una lista de inmuebles (ejemplo)
lista_inmuebles = [
    {'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
    {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
    {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
    {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
    {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
]




def mostrar_menu():
    print("=== Menú de la Inmobiliaria ===\n")
    print("\t1. Agregar inmueble")
    print("\t2. Editar inmueble")
    print("\t3. Eliminar inmueble")
    print("\t4. Cambiar estado de inmueble")
    print("\t5. Buscar inmuebles por presupuesto")
    print("\t6. Salir\n")

def agregar_inmueble(lista):
    os.system('cls')
    print("=== Agregar Inmueble ===")
   

def editar_inmueble(lista):
    os.system('cls')
    print("=== Editar Inmueble ===")
    

def eliminar_inmueble(lista):
    os.system('cls')
    print("=== Eliminar Inmueble ===")
  

def cambiar_estado_inmueble(lista):
    os.system('cls')
    print("=== Cambiar Estado de Inmueble ===")
    

def buscar_inmuebles(lista):
    os.system('cls')
    print("=== Buscar Inmuebles por Presupuesto ===")
  


# Menú principal
while True:
   
    mostrar_menu()
    opcion = input("Ingrese el número de opción deseada: ")

    if opcion == '1':
        agregar_inmueble(lista_inmuebles)
    elif opcion == '2':
        editar_inmueble(lista_inmuebles)
    elif opcion == '3':
        eliminar_inmueble(lista_inmuebles)
    elif opcion == '4':
        cambiar_estado_inmueble(lista_inmuebles)
    elif opcion == '5':
        buscar_inmuebles(lista_inmuebles)
    elif opcion == '6':
        print("Saliendo del programa...")
        break
    else:
        os.system('cls')
        print("*** Opción inválida. Por favor, ingrese un número del 1 al 6 ***\n")



# Miembros del grupo 11

# Martin Elias Zalazar
# David Walter Vargas
# Lucas Brito Lima
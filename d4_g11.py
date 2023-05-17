

# Usamos el modulo del sistema para borrar la consola luego de cada interaccion
import os


# Creamos una lista de inmuebles (ejemplo)
lista_inmuebles = [
    {'año': 2010, 'metros': 150, 'habitaciones': 4,
        'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
    {'año': 2016, 'metros': 80, 'habitaciones': 2,
        'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
    {'año': 2000, 'metros': 180, 'habitaciones': 4,
        'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
    {'año': 2015, 'metros': 95, 'habitaciones': 3,
        'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
    {'año': 2008, 'metros': 60, 'habitaciones': 2,
        'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
]


def mostrar_menu():
    print("=== Menú de la Inmobiliaria ===\n")
    print("\t1. Agregar inmueble")
    print("\t2. Editar inmueble")
    print("\t3. Eliminar inmueble")
    print("\t4. Cambiar estado de inmueble")
    print("\t5. Buscar inmuebles por presupuesto")
    print("\t6. Ver inmuebles")
    print("\t7. Salir\n")


def agregar_inmueble(lista):
    os.system('cls')
    print("=== Agregar Inmueble ===")
    indice = int(input(f"Ingrese el índice del inmueble a agregar mayor o igual a {len(lista)}: "))
    if indice >= len(lista):
        
        inmueble_agregado = {}
        inmueble_agregado['año'] = int(input("Ingrese año de construccion: "))
        inmueble_agregado['metros'] = int(input("Ingrese cantidad de Metros cuadrados: "))
        inmueble_agregado['habitaciones'] = int(input("Ingrese Número de habitaciones: "))
        inmueble_agregado['garaje'] = input("¿Tiene garaje? (S/N): ").upper() == 'S'
        inmueble_agregado['zona'] = input("Zona (A, B o C): ").upper()
        inmueble_agregado['estado'] = input("Estado (Disponible, Reservado o Vendido): ").capitalize()
        
        if validar_inmueble(inmueble_agregado):
            lista[indice].append(inmueble_agregado)  
            print("Inmueble agregado con éxito.")
        else:
            print("Error al agregar el inmueble. Verifica los datos ingresados.")
    else:
        print("Índice inválido. No se encontró el inmueble.")


def editar_inmueble(lista):
    os.system('cls')
    mostrar_inmuebles(lista)
    print("=== Editar Inmueble ===")
    indice = int(input("Ingrese el índice del inmueble a editar: "))
    if indice >= 0 and indice < len(lista):
        inmueble = lista[indice]
        inmueble_nuevo = {}
        inmueble_nuevo['año'] = int(input("Año: "))
        inmueble_nuevo['metros'] = int(input("Metros cuadrados: "))
        inmueble_nuevo['habitaciones'] = int(input("Número de habitaciones: "))
        inmueble_nuevo['garaje'] = input(
            "¿Tiene garaje? (S/N): ").upper() == 'S'
        inmueble_nuevo['zona'] = input("Zona (A, B o C): ").upper()
        inmueble_nuevo['estado'] = input("Estado (Disponible, Reservado o Vendido): ").capitalize()
        if validar_inmueble(inmueble_nuevo):
            lista[indice].update(inmueble_nuevo)  # Actualiza el inmueble en la lista con los nuevos datos
            print("Inmueble editado con éxito.")
        else:
            print("Error al editar el inmueble. Verifica los datos ingresados.")
    else:
        print("Índice inválido. No se encontró el inmueble.")


def eliminar_inmueble(lista):
    os.system('cls')
    print("=== Eliminar Inmueble ===")

    eliminado = int(input("Ingrese el índice del inmueble a eliminar: "))  
    
    print (f"se elimino con exito el inmueble {lista.pop(eliminado)}")


def cambiar_estado_inmueble(lista):
    os.system('cls')
    print("=== Cambiar Estado de Inmueble ===")


def buscar_inmuebles(lista):
    os.system('cls')
    print("=== Buscar Inmuebles por Presupuesto ===")



#  Muestra la lista de inmuebles y sus índices.
def mostrar_inmuebles(lista):
    os.system('cls')
    print("=== Lista de Inmuebles ===")
    for i, inmueble in enumerate(lista):
        print(f"Índice: {i}")
        print(f"Año: {inmueble['año']}")
        print(f"Metros cuadrados: {inmueble['metros']}")
        print(f"Número de habitaciones: {inmueble['habitaciones']}")
        print(f"¿Tiene garaje?: {'Sí' if inmueble['garaje'] else 'No'}")
        print(f"Zona: {inmueble['zona']}")
        print(f"Estado: {inmueble['estado']}")
        print("==========================")

# Verifica si un inmueble cumple con las reglas de validación
def validar_inmueble(inmueble):
    if inmueble['zona'] not in ['A', 'B', 'C']:
        return False
    if inmueble['estado'] not in ['Disponible', 'Reservado', 'Vendido']:
        return False
    if inmueble['año'] < 2000:
        return False
    if inmueble['metros'] < 60:
        return False
    if inmueble['habitaciones'] < 2:
        return False
    return True


#  Calcula el precio de un inmueble según las reglas de precio en función de la zona.
def calcular_precio_inmueble(inmueble):
    metros = inmueble['metros']
    habitaciones = inmueble['habitaciones']
    garaje = inmueble['garaje']
    antiguedad = 2023 - inmueble['año']
    zona = inmueble['zona']

    if zona == 'A':
        precio = (metros * 100 + habitaciones * 500 +
                  garaje * 1500) * (1 - antiguedad / 100)
    elif zona == 'B':
        precio = (metros * 100 + habitaciones * 500 +
                  garaje * 1500) * (1 - antiguedad / 100) * 1.5
    elif zona == 'C':
        precio = (metros * 100 + habitaciones * 500 +
                  garaje * 1500) * (1 - antiguedad / 100) * 2

    return precio


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
        mostrar_inmuebles(lista_inmuebles)
    elif opcion == '7':
        print("Saliendo del programa...")
        break
    else:
        os.system('cls')
        print("*** Opción inválida. Por favor, ingrese un número del 1 al 6 ***\n")


# Miembros del grupo 11

# Martin Elias Zalazar
# David Walter Vargas
# Lucas Brito Lima
# Mauro Erlan

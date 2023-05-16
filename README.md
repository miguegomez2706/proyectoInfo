# Sistema de Gestión de Inmuebles para Inmobiliaria

Este proyecto es un sistema de gestión de inmuebles desarrollado con el objetivo de automatizar sus procesos y facilitar la administración de su inventario. El sistema está diseñado para agregar, editar y eliminar inmuebles de una lista, así como también cambiar el estado de los mismos y realizar búsquedas en función del presupuesto.

## Características

El sistema ofrece las siguientes funcionalidades:

1. **Agregar inmuebles**: Permite ingresar los datos de un nuevo inmueble, como el año de construcción, los metros cuadrados, la cantidad de habitaciones, si cuenta con garaje, la zona en la que se encuentra y su estado (Disponible, Reservado o Vendido). Los inmuebles agregados deben cumplir con las reglas de validación establecidas, como la zona permitida y las restricciones de antigüedad, tamaño y cantidad de habitaciones.

2. **Editar inmuebles**: Permite modificar los datos de un inmueble existente en la lista, brindando la posibilidad de actualizar cualquier atributo del mismo, como el estado, los metros cuadrados, la cantidad de habitaciones, etc. Se deben respetar las reglas de validación al realizar las modificaciones.

3. **Eliminar inmuebles**: Permite eliminar un inmueble de la lista, eliminando todos sus datos de forma permanente.

4. **Cambiar estado de un inmueble**: Permite cambiar el estado de un inmueble sin modificar los demás datos. Por ejemplo, se puede marcar un inmueble como "Reservado" o "Vendido" sin afectar otros atributos como la zona o los metros cuadrados.

5. **Búsqueda de inmuebles por presupuesto**: Permite realizar una búsqueda en la lista de inmuebles en función de un presupuesto máximo dado. El sistema devolverá una lista de inmuebles cuyo precio sea menor o igual al presupuesto especificado, considerando únicamente aquellos inmuebles con estado "Disponible" o "Reservado". Los inmuebles encontrados incluirán un nuevo atributo con su precio, calculado según las reglas de precio establecidas para cada zona.

## Tecnologías utilizadas

El sistema de gestión de inmuebles está desarrollado utilizando los siguientes elementos técnicos:

- Lenguaje de programación: [Python](https://www.python.org/)
- Estructuras de datos: Listas y diccionarios.
- Estructuras de control de flujo: Condicionales y bucles.
- Funciones: Se han utilizado funciones para modularizar y organizar el código.


## Miembros
- Martin Elias Zalazar
- David Walter Vargas
-Lucas Brito Lima
- Agreguen sus nombres chicos....


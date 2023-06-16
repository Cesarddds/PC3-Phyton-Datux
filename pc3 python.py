"""1. Implemente un programa que solicite al usuario una fracción, con
formato X/Y, donde cada uno de X e Y es un número entero, y luego
muestra, como un porcentaje redondeado al número entero más
cercano, donde se indicará la cantidad de combustible en el
tanque. Se debe tener en cuenta los siguientes casos:
- Colocar E en caso X/Y sea menor a 1% del total
- Colocar F en caso X/Y sea mayor a 99%.
- En otro caso, devolver el valor en porcentaje %
También debe tomar en cuenta los siguientes casos:
- X y Y deben ser números enteros
- X debe ser mayor o igual a Y, y Y != 0
De no cumplirse estos casos, se debe volver a preguntar al usuario. Asegúrese de detectar
cualquier excepción como ValueError o ZeroDivisionError.
Ejemplos:
- Input: 4/0 Acción: Volver a preguntar al usuario dada la excepción ZeroDivisionError
- Input 1.5/3 Acción: Error dado que solo se permiten números enteros ValueError
- Input 5/4 Acción: Volver a preguntar al usuario
- Input 3/4 Output: 75%
- Input 4/4: Output F
Nota: Le será de utilidad aplicar"""
while True:
    try:
        fraccion = input("Ingrese una fracción en el formato X/Y: ")
        numerador, denominador = map(int, fraccion.split('/'))
        
        if numerador < 0 or denominador <= 0 or denominador < numerador:
            raise ValueError
        
        porcentaje = (numerador / denominador) * 100
        
        if porcentaje < 1:
            resultado = 'E'
        elif porcentaje > 99:
            resultado = 'F'
        else:
            resultado = str(round(porcentaje)) + '%'
        
        print("Cantidad de combustible en el tanque:", resultado)
        break
    
    except ValueError:
        print("Error: X e Y deben ser números enteros, Y debe ser mayor o igual a X, y Y debe ser diferente de 0.")
    
    except ZeroDivisionError:
        print("Error: El denominador no puede ser 0.")



"""2. Cree un programa que solicite al usuario una lista de calificaciones separadas por comas. Divida
la cadena en calificaciones individuales y almacénelas en una lista para luego convertir cada
calificación en un entero. Deberá utilizar una sentencia try/except para informar al usuario
cuando los valores introducidos no puedan ser convertidos debido a un error de tipeo o
formato. (Los métodos de cadena le serán de utilidad)"""

calificaciones = input("Ingrese una lista de calificaciones separadas por comas: ")
lista_calificaciones = calificaciones.split(",")
calificaciones_enteros = []
for calificacion in lista_calificaciones:
    try:
        calificacion_entero = int(calificacion)
        calificaciones_enteros.append(calificacion_entero)
    except ValueError:
        print(f"Calificación inválida: {calificacion}")
print(calificaciones_enteros)

"""3. Escribe una función de Python que imprima las primeras n filas del triángulo de Pascal.
Nota: El triángulo de Pascal es una figura aritmética y geométrica imaginada por primera vez
por Blaise Pascal."""
    
def triangulo_pascal(n):
    triangulo = []
    for i in range(n):
        fila = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                fila[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
        triangulo.append(fila)
    
    for fila in triangulo:
        print(" ".join(str(num) for num in fila))
triangulo_pascal(5)

"""4. Escriba una función que, dado un string, retorne la longitud de la última palabra. Se considera
que las palabras están separadas por uno o más espacios. También podría haber espacios al
principio o al final del string pasado por parámetro"""

def longitud_ultima_palabra(cadena):
    cadena = cadena.strip()
    palabras = cadena.split()
    return len(palabras[-1])

cadena = input("Ingrese una cadena: ")
longitud = longitud_ultima_palabra(cadena)
print(f"La longitud de la última palabra es {longitud}.")

"""5.Desarrollar un módulo que contenga las siguientes funciones:
● Que genere 20 números enteros aleatorios entre 0 y 100 y devuelva una lista.
● Mostrar la lista obtenida por pantalla.
● Ordenar los valores de la lista y mostrarla por pantalla.
Luego crea un script main.py en el mismo directorio en el que deberás importar el módulo y
ejecutar las funciones.
Nota: utilizar el módulo “random” para generar un número aleatorio. """

Import random

def generar_lista():
    lista = []
    for i in range(20):
        lista.append(random.randint(0, 100))
    return lista

def mostrar_lista(lista):
    print("Lista generada:")
    print(lista)

def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    return lista_ordenada

lista = generar_lista()
mostrar_lista(lista)
lista_ordenada = ordenar_lista(lista)
print("Lista ordenada:")
print(lista_ordenada)

""""6.Cree un módulo llamado operaciones.py el cual contendrá 4 funciones para realizar una suma,
una resta, un producto y una división entre dos números. Todas ellas devolverán el resultado.
En las funciones del módulo deberá de haber tratamiento e invocación manual de errores para
evitar que se quede bloqueada una funcionalidad, esto incluye:
● En caso de que se envíen valores a las funciones que no sean números, deberá
aparecer un mensaje que informe Error: Tipo de dato no válido.
● En caso de realizar una división por cero, deberá aparecer un mensaje que informe
Error: No es posible dividir entre cero.
Una vez creado el módulo, crea un script calculos.py en el mismo directorio en el que deberás
importar el módulo y ejecutar las funciones."""
def suma(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")

def resta(a, b):
    try:
        resultado = a - b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")

def producto(a, b):
    try:
        resultado = a * b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError
        resultado = a / b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")

import operaciones

a = 10
b = 5

print(operaciones.suma(a, b))
print(operaciones.resta(a, b))
print(operaciones.producto(a, b))
print(operaciones.division(a, b))





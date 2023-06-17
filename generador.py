import random

def generar_numeros():
    numeros = []
    for _ in range(20):
        numero = random.randint(0, 100)
        numeros.append(numero)
    return numeros

def mostrar_lista(lista):
    for numero in lista:
        print(numero, end=" ")
    print()

def ordenar_lista(lista):
    lista.sort()
    mostrar_lista(lista)
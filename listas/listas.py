"""Ejercicios

1. Indicar si dos listas son iguales en contenido de elementos
2. Crear una lista que contenga palabras, el usuario decide cuando dejar
de ingresar palabras Luego debe mostrar cuales son palíndromo
3. Indicar si los elementos de dos listas son los mismos independiente al
orden en el que se encuentran
4. Intercambiar todos los elementos de una lista de extremo a extremo 
"""

def listas_iguales(lista1: list, lista2: list) -> str:
    if lista1 == lista2:
        return "Las listas son iguales"

    return "las listas no son iguales"

def palindromos():
    print("Ingrese la cantidad de palabras que desee.")
    print("Para terminar debe escribir SALIR")

    palabras = []
    while True:
        palabra = input("\nIngrese una palabra para ingresarla a la lista: ")
        if palabra.lower() == "salir":
            break

        palabras.append(palabra)

    palindromas = ', '.join([i for i in palabras if i == i[::-1]])
    print(f"\nLas palabras palindromas son: {palindromas}")


def iguales(lista1: list, lista2: list) -> str:
    if lista1.sort() == lista2.sort():
        return "Las listas son iguales"

    return "las listas no son iguales"

def intercambiar(lista: list) -> list:
    return lista[::-1]

if __name__ == "__main__":
    palindromos()
def es_vocal(letra):
    vocales = ["a", "e", "i", "o", "u"]
    print("Es vocal" if letra in vocales else "No es vocal")

def contar_consonantes():
    vocales = ["a", "e", "i", "o", "u"]
    while True:
        cadena = input("\nIngrese una cadena de texto: ")
        if cadena == "FIN":
            break
        
        consonantes = 0
        for caracter in cadena:
            if caracter not in vocales and caracter != " ":
                consonantes += 1
        
        print(f"\nel numero de consonantes es {consonantes}")


def separar(cadena: str):
    vocales = ["a", "e", "i", "o", "u"]
    texto_vocales, texto_consonantes  = '', ''
    for caracter in cadena:
        if caracter not in vocales and caracter != " ":
            texto_consonantes += caracter
        else:
            texto_vocales += caracter

    print(f"\nvocales: {texto_vocales}, consonantes: {texto_consonantes}")

def es_palindromo(cadena):
    print("es palindromo" if cadena == cadena[::-1] else "no es palindromo")

def cambiar_letra(cadena):
    nueva = ''
    for caracter in cadena:
        if caracter.isupper():
            nueva += caracter.lower()
        else:
            nueva += caracter.capitalize()

    print(f"\n{nueva}")

def menu():
    while True:
        print("""\nEjercicios guia strings \n
            1) Verificar si una letra es vocal \n
            2) contar consonantes\n
            3) separar vocales de consonantes\n
            4) Verificar si una palabra es palindromo\n
            5) cambiar cada letra de una palabra por mayúscula y/o minúscula Ejemplo abC ABc\n 
            6) Salir""")

        try:
            opcion = int(input("\nIngese una opcion: "))
        except:
            input("La opcion debe ser un numero presione enter para continuar ")
            continue

        if opcion == 1:
            caracter = input("\nIngrese un caracter: ")
            es_vocal(caracter)
            input("\npresione enter para continuar ")
            continue

        if opcion == 2:
            contar_consonantes()
            input("\npresione enter para continuar ")
        elif opcion == 3:
            cadena = input("\n Ingrese una cadena de texto: ")
            separar(cadena)
            input("\npresione enter para continuar ")
        elif opcion == 4:
            cadena = input("\n Ingrese una cadena de texto: ")
            es_palindromo(cadena)
            input("\npresione enter para continuar ")
        elif opcion == 5:
            cadena = input("\n Ingrese una cadena de texto: ")
            cambiar_letra(cadena)
            input("\npresione enter para continuar ")
        elif opcion == 6:
            break
        else:
            input("Debe ingresar una opciona valida presione enter para continuar")
            continue

menu()
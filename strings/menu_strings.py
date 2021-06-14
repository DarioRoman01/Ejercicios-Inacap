def es_vocal(letra):
    vocales = ["a", "e", "i", "o", "u"]
    print("Es vocal" if letra in vocales else "No es vocal")

def contar_consonantes():
    vocales = ["a", "e", "i", "o", "u"]
    while True:
        cadena = input("\nIngrese una cadena de texto: ")
        if cadena == "FIN":
            break
        consonantes = [x for x in cadena if x not in vocales and x != " "]
        print(f"\nel numero de consonantes es {len(consonantes)}")

def separar(cadena):
    vocales = ["a", "e", "i", "o", "u"]
    texto_consonantes = ''.join([x for x in cadena if x not in vocales])
    texto_vocales = ''.join([x for x in cadena if x in vocales])
    print(f"\nvocales: {texto_vocales}, consonantes: {texto_consonantes}")

def es_palindromo(cadena):
    print("es palindromo" if cadena == cadena[::-1] else "no es palindromo")

def cambiar_letra(cadena):
    cambiada = ''.join(list(map(lambda x: x.lower() if x.isupper() else x.capitalize(), cadena))) 
    print(f"\n{cambiada}")

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
            es_vocal(input("\nIngrese un caracter: "))
            input("\npresione enter para continuar ")
        elif opcion == 2:
            contar_consonantes()
            input("\npresione enter para continuar ")
        elif opcion == 3:
            separar(input("\nIngrese una cadena de texto: "))
            input("\npresione enter para continuar ")

        elif opcion == 4:
            es_palindromo(input("\nIngrese una cadena de texto: "))
            input("\npresione enter para continuar ")

        elif opcion == 5:
            cambiar_letra(input("\nIngrese una cadena de texto: "))
            input("\npresione enter para continuar ")

        elif opcion == 6:
            break
        else:
            input("Debe ingresar una opciona valida presione enter para continuar")
            continue

menu()
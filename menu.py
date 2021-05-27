def ejercicio_a():
    numero = int(input("\ningrese el numero a multiplicar: "))
    multiplicador = int(input("\ningrese el multiplicador: "))
    total = 0
    for i in range(multiplicador):
        total += numero
    print(f"\nel valor de {numero} * {multiplicador} es: {total}")

def ejercicio_b():
    inicio, final = [int(x) for x in input("\nIngrese el inicio y el final separados por espacios: ").split()]
    print([*range(inicio+1, final)])

def ejercicio_c():
    inicio, final = [int(x) for x in input("\nIngrese el inicio y el final separados por espacios: ").split()]
    print([*range(final-1, inicio, -1)])

def ejercicio_d():
    inicio, final = [int(x) for x in input("\nIngrese el inicio y el final separados por espacios: ").split()]
    if inicio > final:
        print([*range(final+1, inicio)])
    else:
        print([*range(final-1, inicio, -1)])

def ejercicio_e():
    cumple, i =  0, 1 
    grupo = int(input("\ningrese la cantidad de niños a analizar: "))

    while i <= grupo:
        peso = float(input(f"\ningrese el peso del niño {i}: "))
        if peso < 1:
            print("el peso no puede ser un numero menor a 1")
            continue

        altura = float(input(f"\ningrese la estatura del niño {i}: "))
        if altura < 0:
            print("la altura no puede ser negativa")
            continue

        edad = int(input(f"\ningrese la edad del niño {i}: "))
        if edad < 0:
            print("la edad no puede ser un numero negativo")
            continue

        if (peso > 40.0) and (altura > 1.30) and ( 11 < edad and edad < 16):
            cumple += 1

        i += 1

    print(f"\n el porcentaje niños que tiene entre 11 y 16 años y miden mas de 1.30 y pesan mas de 40kg es {cumple * 100 / grupo}")

def menu():
    while True:
        print("""\nBienvenido al solucionador de ejercicios\n
        1) multipicar sin operador * \n
        2) mostrar los numeros entre dos numeros de forma acendente\n
        3) mostrar los numeros entre dos numeros de forma decendente\n
        4) mostrar los numeros entre dos numeros si el inicio es mayor
        se mostrara de forma acendente si no de forma decendente\n
        5) Calcular el porcentaje de niños con ciertas caracteristicas en grupo\n 
        6) Salir""")

        opcion = int(input("\nEliga una de las opciones: "))
        if opcion < 1 or opcion > 6:
            input("\nel numero debe ser una de la opciones presione enter para continuar")
            continue

        if opcion == 1:
            ejercicio_a()
            input("\nPresione enter para continuar ")
        elif opcion == 2:
            ejercicio_b()
            input("\nPresione enter para continuar ")
        elif opcion == 3:
            ejercicio_c()
            input("\nPresione enter para continuar ")
        elif opcion == 4:
            ejercicio_d()
            input("\nPresione enter para continuar ")
        elif opcion == 5:
            ejercicio_e()
            input("\nPresione enter para continuar ")
        else:
            break

menu()
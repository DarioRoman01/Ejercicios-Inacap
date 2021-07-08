import random

"""
1. Crear una tupla con los meses del año y se debe solicitar un número al usuario, si el número esta entre 1 y 
la longitud de la tupla, se deberá mostrar el contenido de esa posición, de lo contrario un mensaje de error. El
programa termina cuando el usuario ingresa un 0.

2. Crear una tupla con N números. Luego se debe solicitar un número por teclado y debe determinar cuantas veces
se encuentra dicho número dentro de la tupla.
"""

def errrores(opcion: int):
    if opcion == 1:
        print("Error debe ingresar un numero")
    elif opcion == 2:
        print("Error: no ingreso una opcion valida")

def ejercicio_1():
    meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    )

    while True:
        try:
            mes = int(input("\nIngrese un mes del año con su numero por ejemplo 7(julio): "))
        except:
            print("\nError: debe ingresar un numero!")
            continue

        if mes == 0:
            break

        if mes > 0 and mes <= len(meses):
            print(f"\n{meses[mes-1]}")
        else: 
            print("\nError: no ingreso un mes valido :(")

def ejercicio_2():
    try:
        cantidad = int(input("Ingrese el numero de elementos en la tupla: "))
        if cantidad < 1:
            print("Error: la cantidad de numeros debe ser mayor a 1")
            ejercicio_2()
            return

    except:
        print("Debe ingresar un numero!")
        ejercicio_2()
        return

    nums = tuple([random.randint(1, 101) for _ in range(cantidad)])
    try:
        num = int(input("Ingrese un numero para saber si esta en la tupla: "))
    except:
        print("Debe ingresar un numero!")
        ejercicio_2()
        return

    print(f"El numero {num} se encuentra {nums.count(num)} veces en la tupla")

ejercicio_2()
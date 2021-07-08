from time import sleep

def analizar_sueldos():
    i, sueldo_bajo, sueldos, entre = 1, 0, 0, 0
    while i <= 60:
        try:
            edad = int(input(f"Ingrese la edad de la persona {i}: ")) 
            sueldo = int(input(f"Ingrese el sueldo de la persona {i}: "))
        except ValueError:
            print("Error: Solo se permiten numeros")
            sleep(1)
            continue
        except KeyboardInterrupt:
            print("Error:  Debe tener mas cuidado al ingresar los datos")
            sleep(1)
            continue
        
        sueldos += sueldo
        if sueldo < 450000:
            sueldo_bajo += 1

        if edad > 31 and edad < 40:
            entre += 1

        i += 1


    print(f"La cantidad de personas con sueldos inferiores a 450000 es: {sueldo_bajo}")
    print(f"El promedio de sueldos es: {sueldos / 60}")
    print(f"La cantidad que estan entre 30 y 41 años es: {entre}")
    sleep(1.5)


def analizar_empleados():
    try:
        total = int(input("Ingrese la cantidad de empleados: "))
    except ValueError:
        print("Debe ingresar un numero")
        sleep(1)
        analizar_empleados()
    except KeyboardInterrupt:
        print("Debe tener mas cuidado al ingresar los valores")
        sleep(1.5)
        analizar_empleados()
    
    i = 1
    sueldo_alto = 0
    informatica = 0
    contabilidad = 0
    while i <= total:
        try:
            sueldo = int(input(f"Ingrese el sueldo de la persona {i}: "))
            departamento = input(f"Ingrese el departamento de la persona {i}: ")
        except ValueError:
            print("Debe ingreas un numero")
            sleep(1.5)
            continue
        except KeyboardInterrupt:
            print("Debe tener mas cuidado al ingresar los datos")
            sleep(1.5)
            continue

        if sueldo > 800000 and sueldo < 900000:
            sueldo_alto += 1

        if departamento.lower() == "informatica":
            informatica += 1

        elif departamento.lower() == "contabilidad":
            contabilidad += 1
        
        i += 1

    
    print(f"La cantidad de personas cullo sueldo esta entre 800000 y 900000 es: {sueldo_alto}")
    if informatica > contabilidad:
        print("Hay mas empleados en el departamento de informatica")
    elif informatica < contabilidad:
        print("Hay ma en el departamento de contabilidad")
    else:
        print("Hay las misma cantidad de empleados en el departamento de informatica y contabilidad")   

    sleep(1.5)


def juego_de_cadenas():
    try:
        cadena = input("Ingrese una cadena de texto: ")
    except:
        print("Debe tener mas cuidado al ingresar los datos")
        sleep(1.5)
        juego_de_cadenas()

    print(cadena.upper())
    print(cadena.title())
    print(cadena[::-1])
    print(''.join(list(map(lambda x: x.lower() if x.isupper() else x.capitalize(), cadena))))
    sleep(1.5)


def menu():
    while True:
        print("""
    -----------------------------------------------------------------------------
    |        			Menú Principal   			                            |
    -----------------------------------------------------------------------------
    |   1.- Estadísticas de sueldos y cantidad de personas 		                |
    |   2.- Estadísticas de empleados Empresa.  			                    |
    |   3.- Juegos de Cadenas.  					                            |
    |   4.-  Salir							                                    |
    ----------------------------------------------------------------------------- 
    """)

        try:
            opcion = int(input("Digite Opción-------->  "))
        except ValueError:
            print("Error: La opcion solo puede ser un numero")
            sleep(1.5)
            continue
        except KeyboardInterrupt:
            print("Error: Intenete ingresar la opcino con mas cuidado")
            sleep(1.5)
            continue
        
        if opcion == 1:
            analizar_sueldos()
        elif opcion == 2:
            analizar_empleados()
        elif opcion == 3:
            juego_de_cadenas()
        elif opcion == 4:
            break
        else:
            print("Error: Debe ingresar una opcion valida :(")
            sleep(1.5)
            
            
if __name__ == "__main__":
    menu()
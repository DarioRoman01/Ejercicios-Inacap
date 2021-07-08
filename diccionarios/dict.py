"""
Ejercicios

1. Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono (el nombre no puede
estar vacío y el teléfono al menos debe tener 8 dígitos). Solicitar los contactos hasta que el usuario diga que no
quiere insertar mas. No se podrán ingresar nombres repetidos. Al final mostrar la lista de usuarios con sus
teléfonos.

2. Crear un diccionario que ingrese productos, la clave es el código y ese código tiene asociado, nombre, precio,
stock. Una vez que termine debe mostrar el listado de productos dentro del diccionario. Además indicar el 
producto más caro y el que tiene mayor stock.
"""

def ejercicio_1():
    contactos = {}
    while True:
        nombre = input("\nIngrese el nombre del contacto: ")
        if len(nombre) < 3:
            print("Error: El nombre debe tener un minimo de 3 caracteres")
            continue
        
        telefono = input("\nIngrese el numero del contacto: ")
        if len(telefono) < 8:
            print("Error: El numero de telefono debe tener un minimo de 8 caracteres")
            continue

        if nombre in contactos.keys():
            print("Error: no se permiten nombre duplicados")
            continue
        contactos[nombre] = telefono

        print("\nDesea seguir agregando contactos?")
        continua = input("\nIngrese no para salir. cualquier otra cosa para salir")
        if continua.lower() == "no":
            break

    print(contactos)

        
def ejercicio_2():
    productos = {}
    try:
        n_productos = int(input("Ingrese la cantidad de productos a ingresar: "))
        if n_productos <= 1:
            print("el numero de productos a ingresar debe ser mayor a 1")
            ejercicio_2()
            return 
    except:
        print("Error: Debe ingresar un numero") 
        ejercicio_2()
        return 

    i = 1
    while i <= n_productos:
        codigo = input(f"\ningrese el codigo del producto {i}: ")
        nombre = input(f"\nIngrese el nombre del producto {i}: ")
        
        try:
            precio = int(input(f"\nIngrese el precio del producto {i}: "))
            stock = int(input(f"\nIngrese el stock del producto {i}: "))
        except:
            print("Error: Debe ingresar un numero")
            continue

        productos[codigo] = {"nombre": nombre, "precio": precio, "stock": stock}
        i += 1 

    mas_caro = max(productos, key=lambda key: productos[key]["precio"])
    mas_stock = max(productos, key=lambda key: productos[key]["stock"])

    print(f"\nel producto mas caro es: {productos[mas_caro]['nombre']}")
    print(f"\nel producto con mas stock es: {productos[mas_stock]['nombre']}")

if __name__ == "__main__":
    ejercicio_2()
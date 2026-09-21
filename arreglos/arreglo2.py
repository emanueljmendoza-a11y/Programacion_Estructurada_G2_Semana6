"""
 Create
 Read
 Update
 Delete
Registrar un listado de edades.
"""
edades = []

def agregar_edad(edad):
    edades.append(edad)

def mostrar_edades():
    return edades 

def actualizar_edad(edad, index):
    if 0 <= index < len(edades):
        edades[index] = edad
    else:
        print("Error: El índice ingresado no existe.")

def eliminar_edad(edad):
    if edad in edades:
        edades.remove(edad)
    else:
        print("Error: La edad ingresada no se encuentra en la lista.")

def menu():
    print("""1. Agregar edad
2. editar edad
3. eliminar edad
4. mostrar edades
0. salir""")
    try:
        op = int(input("Digite su opcion[0 - 4]: "))
        return op
    except ValueError:
        return -1

def pedirDatos(mensaje="Digite la edad: "):
    while True:
        try:
            edad = int(input(mensaje))
            return edad  # Se corrigió: antes retornaba 'dato'
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

def seleccionarOpcion():
    op = menu()
    if op == 1:
        edad = pedirDatos("Dime tu edad: ")
        agregar_edad(edad)
    elif op == 2:
        pos = pedirDatos("Dime en que posicion se encuentra: ")
        edad = pedirDatos("Dime la nueva edad: ")
        actualizar_edad(edad, pos)
    elif op == 3:
        edad = pedirDatos("Dime la edad que deseas eliminar: ")
        eliminar_edad(edad)
    elif op == 4:
        print("Edades registradas:", mostrar_edades())
    elif op == 0:
        print("Adios")
        return 0
    else:
        print("Opcion no valida")
    return op

def main():
    # Bucle para mantener el menú activo hasta seleccionar 0
    continuar = -1
    while continuar != 0:
        continuar = seleccionarOpcion()

main()
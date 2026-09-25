edades = []

def agregar(edad):
    edades.append(edad)

def mostrar():
    return edades

def editar(posicion, nueva_edad):
    edades[posicion] = nueva_edad
    
def sacar(posicion):
    return edades.pop(posicion)

def eliminar(edad):
    return edad.remove(edad)
    
agregar(17)
agregar(18)
agregar(20)
editar(2, 19)
agregar(800)
print(sacar(3))
print(eliminar(18))
print(mostrar())
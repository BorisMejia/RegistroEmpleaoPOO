from Registrar import Empleado
def agregar_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    edad = int(input("Ingrese la edad del empleado: "))

    while True:
        salario = float(input("Ingrese el salario del empleado: "))
        if salario >= 0:
            break
        else:
            print("El salario no puede ser negativo. Intente de nuevo.")
    return Empleado(nombre, edad, salario)

def mostrar_empleados(empleados):
    if not empleados:
        print("No hay empleados para mostrar.")
    else:
        print("\nLista de empleados:")
        for idx, empleado in enumerate(empleados):
            print(f"{idx + 1}. {empleado}")

def buscar_empleado(empleados, nombre):
    for empleado in empleados:
        if empleado.nombre == nombre:
            print(f"Empleado encontrado - {empleado}")
            return empleado
    print(f"No se encontró ningún empleado con el nombre '{nombre}'")
    return None

def editar_empleado(empleados):
    nombre_buscar = input("Ingrese el nombre del empleado que desea editar: ")
    empleado = buscar_empleado(empleados, nombre_buscar)

    if empleado:
        empleado.editar()
        print("Empleado editado correctamente.")
    else:
        print(f"No se encontró ningún empleado con el nombre '{nombre_buscar}'")

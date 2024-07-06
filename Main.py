from Funciones import agregar_empleado, mostrar_empleados, buscar_empleado, editar_empleado
def main():
    empleados = []

    while True:
        print("\n1. Agregar empleado")
        print("2. Mostrar empleados")
        print("3. Buscar empleado por nombre")
        print("4. Editar empleado")
        print("5. Salir")
        opcion = input("\nIngrese una opción: ")

        if opcion == '1':
            nuevo_empleado = agregar_empleado()
            empleados.append(nuevo_empleado)
            print("Empleado agregado correctamente.")

        elif opcion == '2':
            mostrar_empleados(empleados)

        elif opcion == '3':
            nombre_buscar = input("Ingrese el nombre del empleado a buscar: ")
            buscar_empleado(empleados, nombre_buscar)

        elif opcion == '4':
            editar_empleado(empleados)

        elif opcion == '5':
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()

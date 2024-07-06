class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.salario}"

    def editar(self):
        print(f"Editar empleado '{self.nombre}':")
        opcion = input("¿Qué desea editar? (nombre/edad/salario): ").lower()

        if opcion == 'nombre':
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            self.nombre = nuevo_nombre
        elif opcion == 'edad':
            nueva_edad = int(input("Ingrese la nueva edad: "))
            self.edad = nueva_edad
        elif opcion == 'salario':
            while True:
                nuevo_salario = float(input("Ingrese el nuevo salario: "))
                if nuevo_salario >= 0:
                    self.salario = nuevo_salario
                    break
                else:
                    print("El salario no puede ser negativo. Intente de nuevo.")
        else:
            print("Opción no válida.")

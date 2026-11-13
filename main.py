
# Propósito: Orquestar el sistema y mostrar el menú interactivo al usuario.

# Importamos las funciones de nuestros otros archivos modulares
from persistencia import cargar
from operaciones import registrar, buscar, listar, actualizar


def main():
    denuncias = cargar()
    opcion = ""
    while opcion != "5":
        print("\n1. Registrar  2. Buscar  3. Listar todas  4. Actualizar estado  5. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            registrar(denuncias)
        elif opcion == "2":
            buscar(denuncias)
        elif opcion == "3":
            listar(denuncias)
        elif opcion == "4":
            actualizar(denuncias)
        elif opcion != "5":
            print("Opción no válida.")



main()

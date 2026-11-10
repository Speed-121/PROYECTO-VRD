

ARCHIVO = "denuncias.txt"


def cargar():
    """Lee el archivo y devuelve una lista de denuncias (diccionarios)."""
    denuncias = []
    try:
        archivo = open(ARCHIVO, "r", encoding="utf-8")
    except FileNotFoundError:
        return denuncias  # si el archivo no existe, no hay denuncias aún
    for linea in archivo:
        partes = linea.strip().split("|")
        if len(partes) == 6:
            denuncias.append({
                "codigo": partes[0], "nombre": partes[1], "dni": partes[2],
                "ubicacion": partes[3], "descripcion": partes[4], "estado": partes[5],
            })
    archivo.close()
    return denuncias


def guardar(denuncias):
    """Escribe todas las denuncias en el archivo, una por línea."""
    archivo = open(ARCHIVO, "w", encoding="utf-8")
    for d in denuncias:
        archivo.write(d["codigo"] + "|" + d["nombre"] + "|" + d["dni"] + "|" +
                      d["ubicacion"] + "|" + d["descripcion"] + "|" + d["estado"] + "\n")
    archivo.close()


def mostrar(d):
    print("-" * 40)
    print("Código     :", d["codigo"])
    print("Nombre     :", d["nombre"])
    print("DNI        :", d["dni"])
    print("Ubicación  :", d["ubicacion"])
    print("Descripción:", d["descripcion"])
    print("Estado     :", d["estado"])


def registrar(denuncias):
    codigo = "D-" + str(len(denuncias) + 1).zfill(4)  # D-0001, D-0002...
    nombre = input("Nombre: ")
    while not nombre.replace(" ","").isalpha():
        nombre=input("Nombre invalido!!!, Use Solo Letras\n")
    dni = input("DNI (8 dígitos): ")
    while len(dni) != 8 or not dni.isdigit():
        dni = input("DNI inválido, escriba 8 dígitos: ")
    ubicacion = input("Ubicación: ").replace("|", " ")
    descripcion = input("Descripción: ").replace("|", " ")
    denuncias.append({"codigo": codigo, "nombre": nombre, "dni": dni,
                      "ubicacion": ubicacion, "descripcion": descripcion,
                      "estado": "Pendiente"})
    guardar(denuncias)
    print("Denuncia guardada con código", codigo)


def buscar(denuncias):
    texto = input("Escriba código, DNI o palabra a buscar: ").strip().lower()
    encontradas = 0
    for d in denuncias:
        if (texto == d["codigo"].lower() or texto == d["dni"]
                or texto in d["descripcion"].lower() or texto in d["ubicacion"].lower()):
            mostrar(d)
            encontradas += 1
    if encontradas == 0:
        print("No se encontró ninguna denuncia.")


def main():
    denuncias = cargar()
    opcion = ""
    while opcion != "4":
        print("\n1. Registrar  2. Buscar  3. Listar todas  4. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            registrar(denuncias)
        elif opcion == "2":
            buscar(denuncias)
        elif opcion == "3":
            for d in denuncias:
                mostrar(d)
        elif opcion != "4":
            print("Opción no válida.")


main()

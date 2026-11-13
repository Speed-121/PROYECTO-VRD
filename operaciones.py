# MÓDULO: operaciones.py
# Propósito: Registrar, buscar, listar y actualizar denuncias.

from persistencia import guardar

ESTADOS = ["Pendiente", "En proceso", "Resuelta", "Rechazada"]

# Mensajes predefinidos para cada estado
MENSAJES = {
    "Pendiente": [
        "Denuncia recibida, en espera de revisión.",
        "Falta información adicional para continuar.",
    ],
    "En proceso": [
        "La denuncia está siendo investigada.",
        "Se derivó el caso al área correspondiente.",
    ],
    "Resuelta": [
        "El caso fue atendido y solucionado.",
        "Se tomaron las acciones necesarias.",
    ],
    "Rechazada": [
        "La denuncia no cumple con los requisitos.",
        "La denuncia es duplicada o ya fue atendida.",
    ],
}


def mostrar(d):
    print("-" * 40)
    print("Código     :", d["codigo"])
    print("Nombre     :", d["nombre"])
    print("DNI        :", d["dni"])
    print("Ubicación  :", d["ubicacion"])
    print("Descripción:", d["descripcion"])
    print("Estado     :", d["estado"])
    if d["mensaje"] != "":
        print("Mensaje    :", d["mensaje"])


def elegir(titulo, opciones):
    """Muestra una lista numerada y devuelve la opción elegida."""
    print(titulo)
    for i in range(len(opciones)):
        print(" ", i + 1, "-", opciones[i])
    eleccion = input("Elija una opción: ")
    while not eleccion.isdigit() or not 1 <= int(eleccion) <= len(opciones):
        eleccion = input("Opción inválida, intente de nuevo: ")
    return opciones[int(eleccion) - 1]


def registrar(denuncias):
    # El código sigue al mayor número existente: D-0001, D-0002...
    mayor = 0
    for d in denuncias:
        numero = d["codigo"][2:]
        if numero.isdigit() and int(numero) > mayor:
            mayor = int(numero)
    codigo = "D-" + str(mayor + 1).zfill(4)

    nombre = input("Nombre: ").strip()
    while not nombre.replace(" ", "").isalpha():
        nombre = input("Nombre inválido, use solo letras: ").strip()
    dni = input("DNI (8 dígitos): ").strip()
    while len(dni) != 8 or not dni.isdigit(): # <- Si la longitud no es 8 o si el contiene caracteres no digitos 
        dni = input("DNI inválido, escriba 8 dígitos: ").strip()
    ubicacion = input("Ubicación: ").replace("|", " ").strip()
    descripcion = input("Descripción: ").replace("|", " ").strip()
    denuncias.append({"codigo": codigo, "nombre": nombre, "dni": dni,
                      "ubicacion": ubicacion, "descripcion": descripcion,
                      "estado": "Pendiente", "mensaje": ""})
    guardar(denuncias)
    print("Denuncia guardada con código", codigo)


def buscar(denuncias):
    texto = input("Escriba código, DNI, nombre o palabra a buscar: ").strip().lower()
    if texto == "":
        print("Debe escribir algo para buscar.")
        return
    encontradas = 0
    for d in denuncias:
        if (texto == d["codigo"].lower() or texto == d["dni"]
                or texto in d["nombre"].lower()
                or texto in d["descripcion"].lower()
                or texto in d["ubicacion"].lower()):
            mostrar(d)
            encontradas += 1
    if encontradas == 0:
        print("No se encontró ninguna denuncia.")


def listar(denuncias):
    if len(denuncias) == 0:
        print("No hay denuncias registradas.")
    for d in denuncias:
        mostrar(d)


def actualizar(denuncias):
    """Cambia el estado de una denuncia y le adjunta un mensaje."""
    if len(denuncias) == 0:
        print("No hay denuncias registradas.")
        return
    codigo = input("Código de la denuncia (ej. D-0001): ").strip().upper()
    denuncia = None
    for d in denuncias:
        if d["codigo"] == codigo:
            denuncia = d
    if denuncia is None:
        print("No existe una denuncia con ese código.")
        return

    mostrar(denuncia)
    nuevo_estado = elegir("\nNuevo estado:", ESTADOS)

    # Mensajes del estado elegido + la opción de escribir uno propio
    opciones = MENSAJES[nuevo_estado] + ["Escribir un mensaje personalizado"]
    mensaje = elegir("\nMensaje para adjuntar:", opciones)
    if mensaje == "Escribir un mensaje personalizado":
        mensaje = input("Escriba su mensaje: ").replace("|", " ").strip()
        while mensaje == "":
            mensaje = input("El mensaje no puede estar vacío: ").replace("|", " ").strip()

    denuncia["estado"] = nuevo_estado
    denuncia["mensaje"] = mensaje
    guardar(denuncias)
    print("Denuncia", codigo, "actualizada a:", nuevo_estado)

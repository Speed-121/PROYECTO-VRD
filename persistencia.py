
# Propósito: Manejar la lectura y escritura en el archivo txt.

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
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        for d in denuncias:
            campos = [d["codigo"], d["nombre"], d["dni"], d["ubicacion"],
                      d["descripcion"], d["estado"], d["mensaje"]]
            archivo.write("|".join(campos) + "\n")

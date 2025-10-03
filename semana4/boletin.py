import re

def comprobar_telefono(telefono):

    patron_tel=r"^(\d{3}-){2}\d{3}$"
    match = re.match(patron_tel,telefono)

    if match:
        return True
    else:
        return False


def comprobar_NIFNIE(nifnie):
    patron = r"^(\d{8}|[XYZ]\d{7})-[TRWAGMYFPDXBNJZSQVHLCKE]$"
    match = re.match(patron, nifnie)
    if match:
        return True
    else:
        return False

def comprobar_fecha(fecha):
    patron1 = r"^(?!0000)\d{4}-((0[1-9])|1[0-2])-(0[1-9]|[12][0-9]|3[01])\s+([01][0-9]|2[0-3]):([0-5]\d)$"
    patron2 = r"(?i)^(January|February|March|April|May|June|July|August|September|October|November|December)\s+([1-9]|[12][0-9]|3[01]),\s+(?!0)([1-9]\d{0,3})\s+([1-9]|1[012]):([0-5]\d)\s+[AP]M$"
    patron3 = r"^([01][0-9]|2[0-3])\:([0-5]\d)\:([0-5]\d)\s+(0[1-9]|[12][0-9]|3[01])\/((0[1-9])|1[0-2])\/(?!0000)\d{4}$"
    match = re.match(patron2, fecha)
    if match:
        return True
    else:
        return False

def comprobar_precio(precio):
    patron = r"^(0\.\d+|[1-9]\d*(\.\d+)?)[€$]$"
    match = re.match(patron, precio)
    if match:
        return True
    else:
        return False

def comprobar_coordenadas(coordenadas):
    patron1 = r"^[-+]?(\d\.\d+|[1-8][0-9]\.\d+|90\.0)(\s*)(\,)(\s*)[-+]?(0\.\d+|[1-9]\d?\.\d+|1[0-7]\d.\d+|180\.0)$"
    patron2 = r"^(\d|[1-8]\d|90)(\°)\s*(\d|[1-5]\d)\'\s*([1-5]?\d\.\d{4})\"\s*[NS]\s*\,\s*((?<!0)\d|[1-9]\d|1[0-7]\d|180)(\°)\s*(\d|[1-5]\d)\'\s*([1-5]?\d\.\d{4})\"\s*[WE]$"
    patron3 = r"^0([0-8]\d|90)([0-5]\d)([0-5]\d\.\d{4})[NS](0\d\d|1[0-7]\d|180)([0-5]\d)([0-5]\d\.\d{4})[WE]$"
    match = re.match(patron3, coordenadas)
    if match:
        return True
    else:
        return False

def main():
    #fichero = input("Ingrese el fichero que desea leer: ")
    #leer(fichero)
    print(comprobar_coordenadas("0300000.0000N0403000.0000W"))
main()
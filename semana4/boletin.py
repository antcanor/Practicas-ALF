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
    patron1 = r"^(?P<formato1>(?P<anio>(?!0000)\d{4})-(?P<mes>((0[1-9])|1[0-2]))-(?P<dia>(0[1-9]|[12][0-9]|3[01]))\s+(?P<hora>([01][0-9]|2[0-3])):(?P<minutos>([0-5]\d))$)"
    patron2 = r"(?i)(?P<formato2>^(?P<mes>(January|February|March|April|May|June|July|August|September|October|November|December))\s+(?P<dia>([1-9]|[12][0-9]|3[01])),\s+(?P<anio>(?!0)([1-9]\d{0,3}))\s+(?P<hora>([1-9]|1[012])):(?P<minutos>([0-5]\d))\s+(?P<horario>[AP]M)$)"
    patron3 = r"(?P<formato3>^(?P<hora>([01][0-9]|2[0-3]))\:(?P<minutos>([0-5]\d))\:(?P<segundos>([0-5]\d))\s+(?P<dia>(0[1-9]|[12][0-9]|3[01]))\/(?P<mes>(0[1-9])|1[0-2])\/(?P<anio>(?!0000)\d{4})$)"
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
    patron1 = r"(?P<formato1>^(?P<signolat>[-+]?)(?P<latitud>(\d\.\d+|[1-8][0-9]\.\d+|90\.0))(\s*)(\,)(\s*)(?P<signolon>[-+]?)(?P<longitud>(0\.\d+|[1-9]\d?\.\d+|1[0-7]\d.\d+|180\.0))$)"
    patron2 = r"(?P<formato2>^(?P<latitud>(\d|[1-8]\d|90))(\°)\s*(?P<minutoslat>(\d|[1-5]\d))\'\s*(?P<segundoslat>([1-5]?\d\.\d{4}))\"\s*(?P<orientacionlat>[NS])\s*\,\s*(?P<longitud>(?<!0)\d|[1-9]\d|1[0-7]\d|180)(\°)\s*(?P<minutoslon>((\d|[1-5]\d)))\'\s*(?P<segundoslon>([1-5]?\d\.\d{4}))\"\s*(?P<orientacionlon>[WE]$))"
    patron3 = r"(?P<formato3>^(?P<latitud>0([0-8]\d|90))(?P<minutoslat>([0-5]\d))(?P<segundoslat>([0-5]\d\.\d{4}))(?P<orientacionlat>[NS])(?P<longitud>(0\d\d|1[0-7]\d|180))(?P<minutoslon>([0-5]\d))(?P<segundoslon>([0-5]\d\.\d{4}))(?P<orientacionlon>[WE])$)"
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
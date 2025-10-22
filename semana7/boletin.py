import regex as re

P_TEL = re.compile(r"^(\d{3}-){2}\d{3}$")
P_DNINIF = re.compile(r"^(\d{8}|[XYZ]\d{7})-[TRWAGMYFPDXBNJZSQVHLCKE]$")
P_INSTANTE = re.compile(r"(?i)^(?P<formato1>(?P<anio>(?!0000)\d{4})-(?P<mes>((0[1-9])|1[0-2]))-(?P<dia>(0[1-9]|[12][0-9]|3[01]))\s+(?P<hora>([01][0-9]|2[0-3])):(?P<minutos>([0-5]\d)))$|^(?P<formato2>(?P<mes>(January|February|March|April|May|June|July|August|September|October|November|December))\s+(?P<dia>([1-9]|[12][0-9]|3[01])),\s+(?P<anio>(?!0)([1-9]\d{0,3}))\s+(?P<hora>([1-9]|1[012])):(?P<minutos>([0-5]\d))\s+(?P<horario>[AP]M))$|^(?P<formato3>(?P<hora>([01][0-9]|2[0-3]))\:(?P<minutos>([0-5]\d))\:(?P<segundos>([0-5]\d))\s+(?P<dia>(0[1-9]|[12][0-9]|3[01]))\/(?P<mes>(0[1-9])|1[0-2])\/(?P<anio>(?!0000)\d{4}))$")
P_COORDENADA = re.compile(r"(?P<formato1>^(?P<signolat>[-+]?)(?P<latitud>(\d\.\d+|[1-8][0-9]\.\d+|90\.0))(\s*)(\,)(\s*)(?P<signolon>[-+]?)(?P<longitud>(0\.\d+|[1-9]\d?\.\d+|1[0-7]\d.\d+|180\.0))$)|(?P<formato2>^(?P<latitud>(\d|[1-8]\d|90))(\°)\s*(?P<minutoslat>(\d|[1-5]\d))\'\s*(?P<segundoslat>([1-5]?\d\.\d{4}))\"\s*(?P<orientacionlat>[NS])\s*\,\s*(?P<longitud>(?<!0)\d|[1-9]\d|1[0-7]\d|180)(\°)\s*(?P<minutoslon>((\d|[1-5]\d)))\'\s*(?P<segundoslon>([1-5]?\d\.\d{4}))\"\s*(?P<orientacionlon>[WE]$))|(?P<formato3>^(?P<latitud>0([0-8]\d|90))(?P<minutoslat>([0-5]\d))(?P<segundoslat>([0-5]\d\.\d{4}))(?P<orientacionlat>[NS])(?P<longitud>(0\d\d|1[0-7]\d|180))(?P<minutoslon>([0-5]\d))(?P<segundoslon>([0-5]\d\.\d{4}))(?P<orientacionlon>[WE])$)")

'''Escribe una función que, dada una cadena de texto con un teléfono, determine si el
formato es válido y, en caso afirmativo, devuelva el número sin espacios en blanco ni
guiones y, en caso de ser un número de 9 dígitos, incluya el prefijo “+34” al comienzo.
Usa las sustituciones de regex para conseguirlo.'''


def comprobar_telefono(telefono):
    tel = P_TEL.fullmatch(telefono)
    if tel is not None:
        tel_singuiones = re.sub(r'\-','',tel.group(0))
        return re.sub(r'^\d{9}$', r'+34\g<0>', tel_singuiones)
    else:
        return None


'''Escribe una función que, dada una cadena de texto con un NIF o NIE, determine si el
formato es válido. En caso afirmativo, comprobará si es correcto (la letra corresponde
al número) usando las funciones de las sesiones anteriores. Si se trata de un NIF
correcto devolverá la cadena original.

'''
def determinar_letra(numero):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    return letras[numero % 23]


def validar_nif(nif):
    # Separar número/letra
    numero, letra = nif.split('-')

    # Sustituir la primera letra si es NIE
    if numero[0] == "X":
        numero = "0" + numero[1:]
    elif numero[0] == "Y":
        numero = "1" + numero[1:]
    elif numero[0] == "Z":
        numero = "2" + numero[1:]

    # Comprobar que el resto son números
    if not numero.isdigit():
        return False

    numero = int(numero)

    # Debe tener 8 cifras
    if not (10000000 <= numero < 1000000000):
        return False

    # Validar la letra
    return letra == determinar_letra(numero)

def comprobarformato_NIFNIE(nif):

    match = P_DNINIF.fullmatch(nif)
    if match:
        if validar_nif(match.group(0)):
            return nif
        else:
            return False
    else:
        return None

'''Escribe una función que, dada una cadena de texto con un instante temporal,
determine si el formato es válido, y en caso afirmativo, extraiga el día, el mes y el año,
la hora, los minutos y los segundos y compruebe si se trata de una fecha y hora válidas
usando las funciones de las sesiones anteriores. En caso afirmativo devolverá una lista
con los seis valores numéricos obtenidos: [ año, mes, día, hora, minutos, segundos ].
'''
def comprobar_instante(instante):
    match = P_INSTANTE.fullmatch(instante)

    try:
        if match:
            if match.group("formato1"):
                print("formato1")
                anio = match.group("anio")
                mes = match.group("mes")
                dia = match.group("dia")
                hora = match.group("hora")
                minutos = match.group("minutos")
                segundos = match.group("segundos")
                checkfecha = fecha_correcta(anio, mes, dia)
                if checkfecha:
                    return [anio, mes, dia, hora, minutos, segundos]
                else:
                    return None
            if match.group("formato2"):
                print("formato2")
                anio = match.group("anio")
                mes = numero_mes(match.group("mes"))
                dia = match.group("dia")
                hora = match.group("hora")
                minutos = match.group("minutos")
                segundos = match.group("segundos")

                checkfecha = fecha_correcta(anio, mes, dia)
                if checkfecha:
                    return [anio, mes, dia, hora, minutos, segundos]
                else:
                    return None

            if match.group("formato3"):
                print("formato3")
                anio = match.group("anio")
                mes = match.group("mes")
                dia = match.group("dia")
                hora = match.group("hora")
                minutos = match.group("minutos")
                segundos = match.group("segundos")

                checkfecha = fecha_correcta(anio, mes, dia)
                if checkfecha:
                    return [anio, mes, dia, hora, minutos, segundos]
                else:
                    return None
    except:
        return None

def numero_mes(mes):
    mes_min = str(mes.lower())
    meses = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
             'november', 'december']
    i = 0
    while i < len(meses):
        if meses[i] == mes_min:
            return i + 1
        i += 1
    return 0

def check_formato_fecha(fecha, hora, formato):
    try:
        if formato == 3:  # HH:MM:SS DD/MM/YYYY
            datos = fecha.split('/')
            if len(datos) != 3:
                return False
            anio = int(datos[2])
            mes = int(datos[1])
            dia = int(datos[0])
            return fecha_correcta(anio, mes, dia)

        elif formato == 1:  # YYYY-MM-DD HH:MM
            datos = fecha.split('-')
            if len(datos) != 3:
                return False
            anio = int(datos[0])
            mes = int(datos[1])
            dia = int(datos[2])
            return fecha_correcta(anio, mes, dia)

        elif formato == 2:  # Mes D, Y HH:MM AM/PM
            dia = int(fecha[1].replace(',', ''))
            mes = numero_mes(fecha[0])
            anio = int(fecha[2])
            return fecha_correcta(anio, mes, dia)

    except:
        return False

    return False

def is_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        return True
    else:
        return False

def fecha_correcta(anio, mes, dia):
    anio = int(anio)
    mes = int(mes)
    dia = int(dia)
    bisiesto = is_bisiesto(anio)
    if dia <= 31:
        if mes <= 12:
            if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                return dia <= 31
            elif mes == 2 and bisiesto:
                return dia <= 29
            elif mes == 2 and not bisiesto:
                return dia <= 28
            else:
                return dia <= 30
        else:
            return False
    else:
        return False
'''Escribe una función que, dada una cadena de texto con una coordenada geográfica
determine si el formato es válido y, en caso afirmativo, extraiga la longitud y latitud de
la coordenada, y compruebe si se trata de un dato correcto. En caso afirmativo
devolverá una lista con los dos valores reales obtenidos: [ latitud, longitud ].'''

def comprobar_coordenada(coordenada):
    match = P_COORDENADA.fullmatch(coordenada)
    try:
        if match:
            if match.group("formato1"):
                print("formato1")
                signolat = match.group("signolat")
                latitud = match.group("latitud")
                signolon = match.group("signolon")
                longitud = match.group("longitud")

                latitud = signolat+latitud
                longitud = signolon+longitud
                return [latitud, longitud]

            if match.group("formato2") or match.group("formato3"):

                latitud = match.group("latitud")
                minutoslat = match.group("minutoslat")
                segundoslat = match.group("segundoslat")
                orientacionlat = match.group("orientacionlat")
                longitud = match.group("longitud")
                minutoslon = match.group("minutoslon")
                segundoslon = match.group("segundoslon")
                orientacionlon = match.group("orientacionlon")

                checkcoordenada = check_coordenada(latitud, minutoslat, segundoslat,longitud, minutoslon, segundoslon)
                if checkcoordenada:
                    latitud = latitud+"º "+minutoslat+"' "+segundoslat+"''"
                    longitud= longitud+"º "+ minutoslon+"' "+segundoslon+"''"
                    return [latitud, longitud]
                else:
                    return None
    except:
        return None

def check_coordenada(latitud, minutoslat, segundoslat, longitud, minutoslon, segundoslon):
    try:
        latitud = int(latitud)
        minutoslat=int(minutoslat)
        segundoslat=float(segundoslat)
        longitud = int(longitud)
        minutoslon=int(minutoslon)
        segundoslon=float(segundoslon)

        if latitud == 90:
            if minutoslat != 0 or segundoslat != 0:
                return False
        if longitud == 180:
            if minutoslon != 0 or segundoslon != 0:
                return False
        return True
    except:
        return False


if __name__ == '__main__':
    #print(comprobar_telefono("123-456-784"))
    #print(comprobarformato_NIFNIE("58469588-T"))
    #print(comprobar_instante("08:15:00 28/09/2001"))
    print(comprobar_coordenada("0300000.0000N0403000.0000W"))

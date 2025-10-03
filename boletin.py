def determinar_letra(numero):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    return letras[numero % 23]


def validar_nif(nif):
    # Separar número/letra
    try:
        numero_str, letra = nif.split('-')
    except:
        return False

    # Sustituir la primera letra si es NIE
    if numero_str[0] == "X":
        numero_str = "0" + numero_str[1:]
    elif numero_str[0] == "Y":
        numero_str = "1" + numero_str[1:]
    elif numero_str[0] == "Z":
        numero_str = "2" + numero_str[1:]

    # Comprobar que el resto son números
    if not numero_str.isdigit():
        return False

    numero = int(numero_str)

    # Debe tener 8 cifras (entre 10 millones y 1.000 millones)
    if not (10000000 <= numero < 1000000000):
        return False

    # Validar la letra
    return letra == determinar_letra(numero)

#comprobamos el numero de digitos que forman el numero de telefono y que estan agrupados en grupos de 3, separados con -
def comprobar_telefono(telefono):
    if len(telefono) == 11:
        grupos = telefono.split('-')
        for grupo in grupos:
            if len(grupo) != 3:
                return False
        return True
    else:
        return False

def comprobar_instante(instante):
    partes = instante.split()

    # Caso 1: "YYYY/MM/DD HH:MM:SS" o "DD-MM-YYYY HH:MM"
    if len(partes) == 2:
        if ":" in partes[0]:
            hora = partes[0]
            fecha = partes[1]
        else:
            hora = partes[1]
            fecha = partes[0]
        if "/" in fecha:
            formato = 3
        else:
            formato = 1

        return check_formato_fecha(fecha, hora, formato)

    # Caso 2: "Day Month Year HH:MM AM/PM"
    elif len(partes) == 5:
        fecha = partes[:3]  # ['12', 'January', '2023']
        hora = partes[3:]   # ['10:30', 'AM']
        return check_formato_fecha(fecha, hora, 2)

    return False

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
            return fecha_correcta(anio, mes, dia) and hora_correcta(hora, formato)

        elif formato == 1:  # YYYY-MM-DD HH:MM
            datos = fecha.split('-')
            if len(datos) != 3:
                return False
            anio = int(datos[0])
            mes = int(datos[1])
            dia = int(datos[2])
            return fecha_correcta(anio, mes, dia) and hora_correcta(hora, formato)

        elif formato == 2:  # Mes D, Y HH:MM AM/PM
            dia = int(fecha[1].replace(',', ''))
            mes = numero_mes(fecha[0])
            anio = int(fecha[2])
            hora_str = hora[0]
            sufijo = hora[1]
            return fecha_correcta(anio, mes, dia) and hora_correcta(hora_str, formato, sufijo)

    except:
        return False

    return False

def hora_correcta(hora_str, formato, sufijo=None):
    try:
        if formato == 3:  # HH:MM:SS
            partes = hora_str.split(':')
            if len(partes) != 3:
                return False
            h = int(partes[0])
            m = int(partes[1])
            s = int(partes[2])
            return 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60

        elif formato == 1:  # HH:MM 24h
            partes = hora_str.split(':')
            if len(partes) != 2:
                return False
            h = int(partes[0])
            m = int(partes[1])
            return 0 <= h < 24 and 0 <= m < 60

        elif formato == 2:  # HH:MM 12h AM/PM
            partes = hora_str.split(':')
            if len(partes) != 2 or sufijo is None:
                return False
            h = int(partes[0])
            m = int(partes[1])
            sufijo = sufijo.upper()
            return 1 <= h <= 12 and 0 <= m < 60 and sufijo in ("AM", "PM")

    except:
        return False

def is_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        return True
    else:
        return False

def fecha_correcta(anio, mes, dia):
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


def leer(fichero):
    try:
        f = open(fichero,"r", encoding="utf-8")
        for linea in f:
            #quitamos los espacios de los extremos
            linea= linea.strip()

            #separamos los datos de cada linea y le quitamos los espacios
            datos = [d.strip() for d in linea.split(';')]

            #comprobamos longitud y asignamos a cada dato una variable
            if len(datos) == 6:
                telefono = datos[0]
                nif = datos[1]
                instante = datos[2]
                coordenada = datos[3]
                producto = datos[4]
                precio = datos[5]


                if comprobar_instante(instante):
                    print(f"ok")
                else:
                    print('Hay error')
            else:
                print("El fichero no sigue el formato")

        f.close()
    except:
        print("El fichero no existe")

def main():
    fichero = input("Ingrese el fichero que desea leer: ")
    leer(fichero)
main()
def isDnioNie(nif):
    if nif[0].isdigit():
        return comprobar_DNI(nif)
    else:
        return comprobar_NIE(nif)

def determinar_letra_DNI(dni) :
    letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
    indice =dni%23
    return letras[indice]

def comprobar_DNI(nif):
    datos = nif.split('-')
    try:
        numeros = int(datos[0])
    except:
        print("El DNI no es valido")
        return False

    letra = datos[1]
    if 1000000000 > numeros > 9999999 and determinar_letra_DNI(numeros)==letra:
        return True
    return False

def comprobar_NIE(nif):
    datos = nif.split('-')
    if len(datos)!=2:
        return False

    primergrupo = datos[0]
    letra = datos[1]
    if primergrupo[0] == 'X':
        primergrupo='0'+primergrupo[1:]
    elif primergrupo[0] == 'Y':
        primergrupo='1'+primergrupo[1:]
    elif primergrupo[0] == 'Z':
        primergrupo='2'+primergrupo[1:]

    try:
        numeros = int(primergrupo)
    except:
        return False
    if numeros<1000000000 and numeros>9999999 and determinar_letra_DNI(numeros)==letra:
        return True
    return False


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
    primeracomprobacion = instante.split(' ')
    if len(primeracomprobacion)==2:
        if ':' in primeracomprobacion[0]:
            return checkFormatoFecha(primeracomprobacion[1], primeracomprobacion[0],3)
        elif ':' in primeracomprobacion[1]:
            return checkFormatoFecha(primeracomprobacion[0], primeracomprobacion[1],1)
    elif len(primeracomprobacion)==5:
        return checkFormatoFecha([primeracomprobacion[1],primeracomprobacion[0],primeracomprobacion[2]], [primeracomprobacion[3],primeracomprobacion[4]],2)

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
def checkFormatoFecha(fecha, hora, formato):
    if formato == 3:
        try:
            datos = fecha.split('/')
            dia = int(datos[2])
            mes = int(datos[1])
            anio = int(datos[0])
        except:
            print("Error")
        return fechaCorrecta(anio,mes,dia) and HoraCorrecta(hora,formato)
    elif formato == 1:
        try:
            datos = fecha.split('-')
            dia = int(datos[0])
            mes = int(datos[1])
            anio = int(datos[2])
        except:
            print("Error")
        return fechaCorrecta(anio, mes, dia) and HoraCorrecta(hora, formato)
    elif formato == 2:
        dia=fecha[0]
        mes=fecha[1].replace(',','')
        anio = fecha[2]
        hora = hora[0]
        tiempo=hora[1]
        return fechaCorrecta(anio, mes, dia) and HoraCorrecta(hora, formato)


def HoraCorrecta(hora, formato):
    if formato==3:
        hora,minuto,segundos = hora.split(':')
        hora = int(hora)
        minuto = int(minuto)
        segundos = int(segundos)
        return hora<24 and minuto<60 and segundos<60
    elif formato==1 or formato==2:
        hora,minuto = hora.split(':')
        hora = int(hora)
        minuto = int(minuto)
        return hora<24 and minuto<60
    return False

def isBisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        return True
    else:
        return False

def fechaCorrecta(anio, mes, dia):
    bisiesto = isBisiesto(anio)
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
            linea= linea.strip()
            datos = [d.strip() for d in linea.split(';')]

            if len(datos)==6:
                telefono = datos[0]
                nif = datos[1]
                instante = datos[2]
                coordenada = datos[3]
                producto = datos[4]
                precio = datos[5]


                if comprobar_telefono(telefono) and isDnioNie(nif) and comprobar_instante(instante):
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
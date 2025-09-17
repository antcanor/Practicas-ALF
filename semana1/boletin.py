import random
na = 0
def isBisiesto(anio):
    if (anio % 4 == 0 and anio % 100!=0) or anio % 400 == 0 :
        return True
    else:
        return False


def fechaCorrecta(anio,mes,dia):
    bisiesto = isBisiesto(anio)
    if dia<=31:
        if mes <= 12:
            if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                return dia<=31
            elif mes == 2 and bisiesto:
                return dia<=29
            elif mes == 2  and not bisiesto:
                return dia<=28
            else:
                return dia<=30
        else:
            return False
    else:
        return False

def compararFechas(anio1, mes1, dia1, hora1, minuto1, segundo1, anio2, mes2, dia2, hora2, minuto2, segundo2):
    if anio1<anio2:
        return -1
    elif anio2<anio1:
        return 1
    elif anio1==anio2:
        if mes1<mes2:
            return -1
        elif mes2<mes1:
            return 1
        elif mes1==mes2:
            if dia1<dia2:
                return -1
            elif dia2<dia1:
                return 1
            elif dia2==dia1:
                if hora1<hora2:
                    return -1
                elif hora2<hora1:
                    return 1
                elif hora2==hora1:
                    if minuto1<minuto2:
                        return -1
                    elif minuto2<minuto1:
                        return 1
                    elif minuto2==minuto1:
                        if segundo1<segundo2:
                            return -1
                        elif segundo2<segundo1:
                            return 1
                        elif segundo2==segundo1:
                            return 0

def generarInstantesTemporales():
    anio = random.randint(0,2025)
    mes = random.randint(1,12)
    dia = random.randint(1,31)
    if fechaCorrecta(anio,mes,dia):
        print(f"{dia}/{mes}/{anio}")
    else:
        generarInstantesTemporales()

def main():
    #anio = int(input("Ingrese el anio: "))
    #print(f"Es bisiesto el {anio}?", isBisiesto(anio))
    #print(fechaCorrecta(2024,2,29))
    #print(compararFechas(2019,1,3,3,45,2,2017,1,3,3,45,2))

    n = 0
    while n < 100:
        generarInstantesTemporales()
        n=n+1

main()
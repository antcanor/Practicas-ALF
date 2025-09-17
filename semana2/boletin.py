import sys


def determinar_letra_DNI(dni) :
    letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
    indice =dni%23
    return letras[indice]

def comprobar_NIF(nif):
    numeros = int(nif[:-1])
    letra = nif[-1]
    if numeros<1000000000 and numeros>9999999 and determinar_letra_DNI(numeros)==letra:
        return True
    return False

def numero_mes(mes):
    mes_min = str(mes.lower())
    meses= ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    i = 0
    while i < len(meses):
        if meses[i] == mes_min:
            return i+1
        i += 1
    return 0

def separar_productos(productos):
    productos = productos.split(';')

    producto_limpio = list(p.strip() for p in productos)
    return producto_limpio


def main() :
    #dni = '58469588T'
    #print(comprobar_NIF(dni))

    #prod = "  Pan ;  Leche; Huevos ;  Queso ; Yogur  "
    #print(separar_productos(prod))
    for arg in sys.argv[1:] :
        if len(str(arg))==9 and arg.isalnum():
            print(comprobar_NIF(str(arg)))
        elif arg.isalpha():
            print(numero_mes(arg))
        else :
            print(separar_productos(arg))



main()
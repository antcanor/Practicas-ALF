import random

edad = 5+(3*9)/2
peso = 50.5
nombre = "Juan"
permiso=not(edad>18) or peso <=20 and nombre !="Pepe"
'''
if edad> 18 :
    print("Eres grande")
    print("Puedes entrar")
else:
    print("Eres pequeño")
    print("No puedes entrar")
'''
'''
    Esta funcion suma dos numeros 
'''
def saluda() :
    print("Hola")
    print("Pepe")

def suma(a, b):
    global edad
    edad = 3
    return a+b+edad

def main() :
    n = 0
    while n < 10 :
        print(n, random.randint(0,10))
        n=n+1


main()
import modulo
from modulo import func,variable

'''f = open("log.csv","w", encoding="utf-8")
#tod = f.read()
#linea= f.readline()
while linea:
    print(linea)
    linea = f.readline()

for linea in f:
    print(linea)

f.close()'''

f= open("salida.txt", "w", encoding="utf-8")
f.write("Hola")
print("Hola", file=f)
f.close()

modulo.func()
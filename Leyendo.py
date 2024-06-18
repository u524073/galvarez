fichero = open('C:\\Users\\u524073\\Desktop\\Python\\WS.csv')
print(fichero.read())

salida = open('C:\\Users\\u524073\\Desktop\\Python\\salida.csv', "a")
fichero = open('C:\\Users\\u524073\\Desktop\\Python\\WS.csv')
caracter = fichero.readline(1)
while caracter != "":
    if caracter == '|': salida.write(';')
    else: salida.write(caracter)
    caracter = fichero.readline(1)
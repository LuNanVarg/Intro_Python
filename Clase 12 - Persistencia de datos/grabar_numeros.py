import json

numeros = [1,3,6,8,99]

filename  = 'C:/Users/Luna/Desktop/IntroPython/Clase 12 - Persistencia de datos/numeros.json'
with open(filename, 'w') as archivo:
    json.dump(numeros, archivo) #grabar mi lista a archivo(filename)

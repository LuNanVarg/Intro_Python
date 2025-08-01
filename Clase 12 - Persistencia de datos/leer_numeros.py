#leer_numeros.py
import json

filename = 'numeros.json'
with open(filename) as archivo:
    numeros = json.load(archivo) #cargamos la info en una vble
    
print(type(numeros))
print(numeros)

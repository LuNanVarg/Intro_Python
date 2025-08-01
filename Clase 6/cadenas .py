#for
#iterar en cadenas

cadena = "Hola mundo!"

print(len(cadena)) 
print(cadena[2]) #1
print(cadena[-1]) #!
print(cadena[15]) # -1 - IndexError

for letra in cadena: 
    print(letra)
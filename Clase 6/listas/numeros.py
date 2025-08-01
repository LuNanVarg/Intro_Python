# haciendo una lista numérica

for valor in range(1,6): # range(inicio, fin, paso)
    print(valor) 

# usando range() para una lista numérica
numeros = list(range(1,6)) #Inicio, fin, por defecto paso=1
print(numeros)
print(type(numeros))

#numeros pares
numeros_pares = list(range(2,11,2)) #inicio, fin, paso
print(numeros_pares)

#estadisticas simples
digitos = [1, 3, 5, 9, 7, 4]
print(min(digitos))
print(max(digitos))
print(sum(digitos))


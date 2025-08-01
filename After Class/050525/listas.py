
frutas = ["naranjas", "uva", "banana", "ananá", "ciruela"]

print(frutas[4]) #ciruela
ultima_fruta = frutas[-1]
print(ultima_fruta)

# 560
# 1235
# 875
# 667
ingresos = [560, 1235, 875, 667]

contador = 0

while contador < 3:

    print("Intento:", contador)

    contador += 1
    
for i in range(2, 10, 2):

    print(i)
    
lista = ["A", "B", "C"] #len(lista)

for i in range(len(lista)): #range(3) =>lista numerica 3 => 0,1,2
    print(f"Elemento {i+1}: {lista[i]}")
    
numeros = [10, 20, -30, 40, -50]

suma = 0

for numero in numeros:

    if numero < 0:

        continue

    suma += numero

print(suma)
    

#user.py
#recorrer diccionarios
user = {
    'username': 'efermi',
    'name': 'enrico',
    'last' : 'fermi'
}

#accedemos a clave y valor
#for key, value in user.items()
#for k, v in user.items()
for clave, valor in user.items():
    print(f"Clave: {clave}", end=" - ")
    print(f"Valor: {valor}")

#accedemos a las claves
for k in user.keys():
    print(f"Clave: {k}")
    
#accedemos a los valores
for v in user.values():
    print(f"Valor: {v}")
#lenguajes.py
lenguajes_favoritos = {
    'jenifer': 'java',
    'sara': 'php',
    'eduardo': 'c',
    'pedro': 'python',
    'luis': '.net',
    'maria': '.net',
}

for nombre, lenguaje in lenguajes_favoritos.items():
    print(f" A {nombre.title()} le gusta el lenguaje {lenguaje.title()}")
  
#operador de pertenencia
nombre_input = input("Ingrese nombre de la persona que quiere verificar: ")  
if nombre_input in lenguajes_favoritos.keys():
    print(f"{nombre_input.title()} respondió que le gusta el lenguaje {lenguaje.title()}")
else:
    print(f"{nombre_input} no respondió la encuesta.")
    
print(lenguajes_favoritos.get('maria')) #.net

#recorrer un diccionario ordenando por las claves
for nombre in sorted(lenguajes_favoritos.keys()):
    print(f"{nombre.title()} gracias por responder la encuesta")

#mascota3.py

#ambito de la variable - local o global
edad = input("Ingrese edad: ") #variable global - esto es lo recomendado
# parámetros por default, o por defecto
def describir_mascota(nombre_mascota, tipo_animal = 'gato'): #parámetro con un valor por defecto
    '''
    describe la mascota
    '''
    #global edad #convirtiendo la variable local - no es lo recomendado
    #edad = input("Ingrese edad: ") #variable local
    print(edad)
    print(f"Tengo un {tipo_animal} y se llama {nombre_mascota.title()}")

#Principal
#invocación equivalente 
describir_mascota("Kala", "perro") 
#edad = input("Ingrese edad: ") #variable global
print(edad)
describir_mascota("Elsa") #argumentos posicionales
describir_mascota(nombre_mascota="Ramon")
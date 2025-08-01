#mascota2.py
# parámetros por default, o por defecto
def describir_mascota(nombre_mascota, tipo_animal = 'gato'): #parámetro con un valor por defecto
    '''
    describe la mascota
    '''
    print(f"Tengo un {tipo_animal} y se llama {nombre_mascota.title()}")

#Principal
#invocación equivalente 
describir_mascota("Kala", "perro") 
describir_mascota("Elsa") #argumentos posicionales
describir_mascota(nombre_mascota="Ramon")

def describir_mascota(tipo_animal, nombre_mascota):
    '''
    describe la mascota
    '''
    print(f"Tengo un {tipo_animal} y se llama {nombre_mascota.title()}")

#Principal
describir_mascota("gato", "Elsa")
describir_mascota("perro", "Kala") #argumentos posicionales
tipo = input("Tipo: ")
nombre = input("Nombre: ")
describir_mascota(tipo, nombre)
# invocar a la funcion pasando argumentos por sus nombres(parámetro)
describir_mascota(nombre_mascota='Json', tipo_animal='gato')

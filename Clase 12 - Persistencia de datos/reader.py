# filename = "C:/Users/Luna/Desktop/IntroPython/Clase 12 - Persistencia de datos/alice.txt"
def contar_palabras(filename):
    '''Contar las palabras de los libros que paso como parametro.'''
    try: 
        with open(filename) as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print(f"El archivo {filename} no existe")
    else:
        palabras = contenido.split()
        num_palabras = len(palabras)
        print(f"El archivo {filename} tiene {num_palabras} palabras.")
        

filenames = ['C:/Users/Luna/Desktop/IntroPython/Clase 12 - Persistencia de datos/alice.txt','siddhartha.txt', 'moby_dick.txt']
for filename in filenames:
    contar_palabras(filename)
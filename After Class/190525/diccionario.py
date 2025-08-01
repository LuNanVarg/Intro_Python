'''
Ejercicio Clase 8:

Crear un diccionario llamado productos donde las claves sean los nombres de los productos y los valores sean sus precios. 

Permitir que se agreguen productos y sus precios hasta que se decida finalizar. 

Mostrar el contenido del diccionario después de cada operación.

'''

productos = {
    #nombre del articulo: precio
    "paraguas" : 3000,
    "botas" : 5000.50,
    "sombrillas" : [5000, 2500, 7500],
    "otros" : {
            "antejos" : 5200,
            "protector solar" : 15000,
    }
}

while True:
    # alta 
    nombre_input = input("Ingrese nombre: ")
    precio_input = input("Ingrese precio: ")

    # # VALIDAR!
    productos[nombre_input] = precio_input

    # mostrar luego de cada ingreso de datos
    for nombre, precio in productos.items():
        #print(type(precio))
        if type(precio) == list:
            print(f"{nombre}: ")
            for pr in precio:
                print(f"\t ${pr}")
        elif type(precio) == dict:
            print(f" {nombre}: ")
            for c,v in precio.items():
                print(f"\t {c} : ${v}")
        else:
            print(f"{nombre}: ${precio}")
        
    opcion = input("Desea cargar más productos?: (S/N)").lower()
    if opcion != 's':
        break 


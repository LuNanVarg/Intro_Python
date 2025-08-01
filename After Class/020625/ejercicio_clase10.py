'''
Eliminar productos: A partir de su nombre.

 Menú interactivo: Debe ofrecer un menú para que se pueda elegir qué acción realizar.'''
 
productos = []

def validar_nombre(nombre_producto):
    if nombre_producto != '':
        return True
    else:
        return False
    
def validar_precio(precio_producto):
    if precio_producto != '' and precio_producto.isdigit():
        return True
    else:
        return False

def agregar_productos():
    '''
    Permite a la usuaria o usuario agregar productos a una lista, con nombre y precio.
    '''
    nombre = input("Ingrese nombre del producto: ").strip().lower()
    precio = input("Ingrese precio del producto: ").strip()
    
    while not validar_nombre(nombre):
        print("Ingrese nombre válido: ")
        nombre = input()
    #verificar la existencia de un nombre previamente creado
    while not validar_precio(precio):
        print("Ingrese precio válido: ")
        precio = input()   
    producto = [nombre, float(precio)]
    productos.append(producto)  
    print("Producto añadido con éxito! ")
    

def consultar_productos():
    '''
    Muestra todos los productos en la lista junto con sus precios
    '''
    print("Listado de productos: ")
    for producto in productos:
        print(f"Nombre: {producto[0]}")
        print(f"Precio: {producto[1]:.2f}")
        
def consultar_producto(): #individual, producto particular
    pass

def eliminar_productos():
    '''A partir de su nombre'''
    if not productos:
        print("No hay productos disponibles para eliminar")
    else:
        nombre = input("Ingrese nombre del producto a eliminar: ").strip().lower()
        while not validar_nombre(nombre):
            int("Ingrese nombre válido: ")
            nombre = input()
        #si existen repetidos
        #creo una lista de repetidos
        lista_repetidos = []
        #recorren la lista de productos eliminando  los repetidos
        for producto in productos:
            if producto in lista_repetidos:
                pass
                #elimino producto
                 
        
        
def menu_principal():
    print("=" * 40)
    print("       🛒 Menú de Tienda - CRUD       ")
    print("=" * 40)
    print("1. Agregar producto")
    print("2. Consultar producto")
    print("3. Eliminar producto")
    print("4. Salir")
    print("=" * 40)
    
    

# principal
opcion = "" #global
while True:
    menu_principal()
    opcion = input("Selecciona una opción (1-4): ").strip()
    while not (opcion.isdigit() and 1 <= int(opcion) <= 4):
        print("❌ Opción inválida.")
        opcion = input("Selecciona una opción (1-4): ").strip()

    opcion = int(opcion)

    match opcion:
        case 1:
            agregar_productos()
        case 2:
            consultar_productos()
        case 3: 
            eliminar_productos()
        case 4:
            print("saliendo...")
            break
       
productos = []

def validar_nombre(nombre_producto):
    return nombre_producto != ''
    
def validar_precio(precio_producto):
    return precio_producto != '' and precio_producto.replace('.', '', 1).isdigit()

def agregar_productos():
    '''
    Permite a la usuaria o usuario agregar productos a una lista, con nombre y precio.
    '''
    nombre = input("Ingrese nombre del producto: ").strip().lower()
    while not validar_nombre(nombre):
        print("⚠️ Ingrese nombre válido:")
        nombre = input().strip().lower()

    precio = input("Ingrese precio del producto: ").strip()
    while not validar_precio(precio):
        print("⚠️ Ingrese precio válido:")
        precio = input().strip()

    producto = [nombre, float(precio)]
    productos.append(producto)
    print("✅ Producto añadido con éxito!\n")

def consultar_productos():
    '''
    Muestra todos los productos en la lista junto con sus precios
    '''
    if not productos:
        print("📭 No hay productos registrados.\n")
    else:
        print("\n📋 {:^40}".format("LISTADO DE PRODUCTOS"))
        print("-" * 40)
        print("{:<3} {:<20} {:>10}".format("N°", "Producto", "Precio ($)"))
        print("-" * 40)
        for i, producto in enumerate(productos, 1):
            print("{:<3} {:<20} {:>10.2f}".format(i, producto[0], producto[1]))
        print()

def eliminar_productos():
    '''
    Elimina todos los productos con el nombre indicado.
    '''
    
    global productos #modifica una variable global en un entorno local
    if not productos:
        print("❌ No hay productos disponibles para eliminar.\n")
        return #vuelve al punto que invocó sin retornar valor

    nombre = input("Ingrese nombre del producto a eliminar: ").strip().lower()
    while not validar_nombre(nombre):
        print("⚠️ Ingrese nombre válido:")
        nombre = input().strip().lower()

    # Contamos cuántos productos se eliminaron
    cantidad_eliminados = 0
    # Filtramos todos los productos que NO coinciden con el nombre a eliminar
    
    nueva_lista = []
    for producto in productos:
        if producto[0] == nombre:
            cantidad_eliminados += 1
        else:
            nueva_lista.append(producto)

    productos = nueva_lista

    if cantidad_eliminados > 0:
        print(f"🗑️ Se eliminaron {cantidad_eliminados} producto(s) con el nombre '{nombre}'.\n")
    else:
        print(f"❌ No se encontraron productos con el nombre '{nombre}'.\n")

def menu_principal():
    print("=" * 40)
    print("       🛒 Menú de Tienda - CRUD       ")
    print("=" * 40)
    print("1. Agregar producto")
    print("2. Consultar productos")
    print("3. Eliminar producto")
    print("4. Salir")
    print("=" * 40)

# principal
opcion = ""
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
            print("👋 Saliendo del programa...")
            break

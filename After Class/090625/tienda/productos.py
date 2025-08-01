import random
import datetime
from colorama import Fore, Style, init
init(autoreset=True)

productos = []

def validar_nombre(nombre_producto):
    return nombre_producto != ''
    
def validar_precio(precio_producto):
    #return precio_producto != '' and precio_producto.replace('.', '', 1).isdigit()
    try:
        float(precio_producto)
        return True
    except ValueError:
        return False

def agregar_productos():
    '''
    Permite a la usuaria o usuario agregar productos a una lista, con nombre y precio.
    '''
    nombre = input(Fore.YELLOW + "Ingrese nombre del producto: ").strip().lower()
    while not validar_nombre(nombre):
        print(Fore.RED + "⚠️ Ingrese nombre válido:")
        nombre = input().strip().lower()

    precio = input(Fore.YELLOW + "Ingrese precio del producto: ").strip()
    while not validar_precio(precio):
        print(Fore.RED + "⚠️ Ingrese precio válido:")
        precio = input().strip()

    id_producto = random.randint(1000, 9999)
    fecha_agregado = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #producto = [nombre, float(precio)]
    producto = {
        "id": id_producto,
        "nombre" : nombre,
        "precio" : float(precio),
        "fecha" : fecha_agregado
    }
    productos.append(producto)
    print(Fore.GREEN + f"✅ Producto {nombre} añadido con éxito! (ID: {id_producto})\n")

def consultar_productos():
    '''
    Muestra todos los productos en la lista junto con sus precios
    '''
    if not productos:
        print("📭 No hay productos registrados.\n")
    else:
        print("\n📋 {:^40}".format("LISTADO DE PRODUCTOS"))
        print("-" * 40)
        print("{:<3} {:<10} {:>10} {:>10}".format("N°", "Producto", "Precio ($)", "Fecha Creación"))
        print("-" * 40)
        # for i, producto in enumerate(productos, 1):
        #     print("{:<3} {:<10} {:>10.2f} {:<10}".format(producto[id], producto[nombre], producto[1]))
        for producto in productos:
            print(Fore.CYAN + "{:<3} {:<10} {:>10.2f} {:<10}".format(producto['id'], producto['nombre'], producto['precio'], producto['fecha']))
        # for producto in productos:
        #     print(Fore.CYAN + f"ID: {producto['id']}")
        #     print(Fore.CYAN + f"Nombre: {producto['nombre']}")
        #     print(Fore.CYAN + f"Precio: {producto['precio']:.2f}")
        #     print(Fore.CYAN + f"Fecha agregado: {producto['fecha']}")
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
    
    nueva_lista = [] #productos filtrados
    for producto in productos:
        if producto['nombre'] == nombre:
            cantidad_eliminados += 1
        else:
            nueva_lista.append(producto)

    productos = nueva_lista

    if cantidad_eliminados > 0:
        print(f"🗑️ Se eliminaron {cantidad_eliminados} producto(s) con el nombre '{nombre}'.\n")
    else:
        print(f"❌ No se encontraron productos con el nombre '{nombre}'.\n")

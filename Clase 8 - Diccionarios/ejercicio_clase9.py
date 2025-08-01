 """  Tarea:
Agregar productos: Permite agregar productos a una lista. Cada producto debe tener un nombre, precio.
Consultar productos: Muestra todos los productos en la lista junto con sus precios.
Eliminar productos: Eliminar un producto de la lista a partir de su nombre.
Menú interactivo: El programa debe ofrecer un menú para que se pueda elegir qué acción realizar.
 """

productos = [] #global

def agregar_producto():
   nombre = input("Nombre: ")
   precio = input("Precio: ")
   #validar
def consultar_productos():
   '''
   Muestra todos los productos en la lista junto con sus precios.
   '''
   if productos:
      #recorrer la lista
      print(productos)
   else:
      print("No hay productos registrados.")

def eliminar_producto():
   pass

def mostrar_menu():
    print("=" * 40)
    print("       🛒 Menú de Tienda - CRUD       ")
    print("=" * 40)
    print("1. Agregar producto")
    print("2. Consultar producto")
    print("3. Eliminar producto")
    print("4. Salir")
    print("=" * 40)

    opcion = input("Selecciona una opción (1-4): ").strip()
    while not (opcion.isdigit() and 1 <= int(opcion) <= 4):
        print("❌ Opción inválida.")
        opcion = input("Selecciona una opción (1-4): ").strip()

    opcion = int(opcion)

    match opcion:
        case 1:
          agregar_producto()
        case 2:
          consultar_productos()
        case 3:
          eliminar_producto()
        case 4:
          print("Saliendo...")
          #break

# Principal
opcion = "" #global 
while opcion != 4:
    mostrar_menu()
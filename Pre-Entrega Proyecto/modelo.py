#
#
#
productos = [
    ["Servicio de Copiado - Hoja a color", "Servicios", 500],
    ["Servicio de Copiado - Hoja B/N", "Servicios", 200],
    ["Cuaderno A4", "Papelería", 5500],
    ["Papel Lunares 2 Hojas Colores Surtidos", "Papelería", 1500],
    ["Folio Escolar Luma Borde Color 10 Unidades", "Papelería", 2300],
    ["Bloc De Dibujo Nro 5 EL NENE Blanco 24 Unidades", "Papelería", 7190],
    ["Lapicera Parker", "Regalería", 3500],
    ["Boligrafo FILGO Gel Pop Glitter 10 Unidades", "Regalería", 9500],
    ["Adhesivo Escolar PELIKAN 30 Ml 1 Unidad", "Regalería", 1200],
    ["RESALTADOR PELIKAN FLASH", "Regalería", 2050],
    ["Agenda Pocket Galaxia", "Regalería", 9990],
    ["Cartuchera Objetos", "Regalería", 8710]
]

# Función para mostrar menú
def mostrar_menu():
    print("=" * 40)
    print("       Menu de Tienda - CRUD       ")
    print("=" * 40)
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("=" * 40)

# Mostrar menú inicial
mostrar_menu()

opcion = input("Seleccioná una opción (1-5): ")
while not(opcion.isdigit() and 1 <= int(opcion) <= 5):
    print("Opción inválida.")
    opcion = input("Seleccioná una opción (1-5): ")

opcion = int(opcion)

while opcion != 5:
    match opcion:
        case 1:
            # Agregar producto
            print("======== Agregar producto ============")
            nombre = input("Nombre del producto: ").strip().title()
            categoria = input("Categoría: ").strip().title()
            precio = input("Precio (sin centavos): ").strip()

            if nombre and categoria and precio:
                if precio.isdigit():
                    precio = int(precio)
                    producto = [nombre, categoria, precio]
                    productos.append(producto)
                    print(f"Producto '{nombre}' agregado.")
                else:
                    print("El precio debe ser un número entero válido.")
            else:
                print("Todos los campos son obligatorios.")
        
        case 2:
            # Ver productos
            print("======== Productos registrados ============")
            if not productos:
                print("No hay productos registrados.")
            else:
                for i, producto in enumerate(productos, 1):
                    print(f"{i}. {producto[0]} ({producto[1]}) - ${producto[2]}")

        case 3:
            # Buscar producto
            print("======== Búsqueda de productos ============")
            if not productos:
                print("No hay productos registrados.")
            else:
                nombre_buscar = input("Ingresá el nombre del producto: ").strip().title()
                encontrados = []
                for producto in productos:
                    if producto[0] == nombre_buscar:
                        encontrados.append(producto)
                if encontrados:
                    print(" Resultados encontrados:")
                    for i, producto in enumerate(encontrados, 1):
                        print(f"{i}. {producto[0]} ({producto[1]}) - ${producto[2]}")
                else:
                    print(f"No se encontró ningún producto llamado '{nombre_buscar}'.")

        case 4:
            # Eliminar producto
            print("======== Eliminar producto ============")
            if not productos:
                print("No hay productos registrados.")
            else:
                for i, producto in enumerate(productos, 1):
                    print(f"{i}. {producto[0]} ({producto[1]}) - ${producto[2]}")
                pos = input("Número del producto a eliminar: ")
                while not (pos.isdigit() and 1 <= int(pos) <= len(productos)):
                    print("Ingresá una posición válida.")
                    pos = input("Número del producto a eliminar: ")
                eliminado = productos.pop(int(pos) - 1)
                print(f"Producto '{eliminado[0]}' eliminado.")

    # Volver a mostrar menú
    mostrar_menu()
    opcion = input("Seleccioná una opción (1-5): ")
    while not(opcion.isdigit() and 1 <= int(opcion) <= 5):
        print("Opción inválida.")
        opcion = input("Seleccioná una opción (1-5): ")
    opcion = int(opcion)

print("¡Programa finalizado!")

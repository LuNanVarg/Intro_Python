# Mi lista de productos: [Nombre, Categoría, Precio]
productos = [
    ["Servicio de Copiado - Hoja a color", "Servicios", 500],
    ["Servicio de Copiado - Hoja B/N", "Servicios", 200],
    ["Cuaderno A4", "Papelería", 5500],
    ["Papel Lunares 2 Hojas Colores Surtidos1", "Papelería", 1500],
    ["Bloc De Dibujo Nro:5 Blanco 24 Unidades", "Papelería", 7190],
    ["Lapicera Parker", "Regalería", 3500],
    ["Bolígrafo FILGO Gel Pop Glitter 10 Unidades", "Regalería", 9500],
    ["Agenda Pocket Galaxia", "Regalería", 9990],
    ["Cartuchera Objetos", "Regalería", 8710]
]

def mostrar_menu():
    print("=" * 50)
    print("     🛍️ Regalería & 📚 Librería      ")
    print("=" * 50)
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("=" * 50)

opcion = ""
while opcion != 5:
    mostrar_menu()
    opcion = input("Seleccioná una opción (1-5): ").strip()

    while not(opcion.isdigit() and 1 <= int(opcion) <= 5):
        print("❌ Opción inválida.")
        opcion = input("Seleccioná una opción (1-5): ").strip()
    opcion = int(opcion)

    match opcion:
        case 1:
            print("======= 📝 Agregar producto =======")
            nombre = input("Nombre del producto: ").strip().title()
            categoria = input("Categoría (Papelería, Regalería, Servicios): ").strip().title()
            precio = input("Precio sin centavos: ").strip()

            datos_ok = True

            if not nombre or not categoria or not precio:
                print("❌ Todos los campos son obligatorios.")
                datos_ok = False

            if datos_ok and not precio.isdigit():
                print("❌ El precio debe ser un número entero.")
                datos_ok = False
            else:
                precio = int(precio)

            if datos_ok:
                producto = [nombre, categoria, precio]
                productos.append(producto)
                print(f"✔ Producto '{nombre}' agregado.")
            else:
                print("❌ No se pudo agregar el producto.")

        case 2:
            print("======= 📦 Lista de productos =======")
            if not productos:
                print("❌ No hay productos registrados.")
            else:
                print("\n📋 {:^60}".format("LISTADO DE PRODUCTOS"))
                print("-" * 60)
                print("{:<3} {:<35} {:<12} {:<8}".format("N°", "Producto", "Categoría", "Precio"))
                print("-" * 60)

                for i, producto in enumerate(productos, 1):
                    print("{:<3} {:<35} {:<12} ${:<8}".format(i, producto[0], producto[1], producto[2]))

        case 3:
            print("======== 🔍 Buscar producto ============")
            if not productos:
                print("❌ No hay productos registrados.")
            else:
                nombre_buscar = input("🔍 Ingresá el nombre del producto: ").strip().title()
                encontrados = [p for p in productos if p[0] == nombre_buscar]

                if encontrados:
                    print("📝 Resultados encontrados:")
                    print("-" * 60)
                    print("{:<3} {:<35} {:<12} {:<8}".format("N°", "Producto", "Categoría", "Precio"))
                    print("-" * 60)
                    for i, producto in enumerate(encontrados, 1):
                        print("{:<3} {:<35} {:<12} ${:<8}".format(i, producto[0], producto[1], producto[2]))
                else:
                    print(f"❌ No se encontró ningún producto llamado '{nombre_buscar}'.")

        case 4:
            print("======== 🗑️ Eliminar producto ============")
            if not productos:
                print("❌ No hay productos registrados.")
            else:
                print("\n📋 {:^60}".format("LISTADO DE PRODUCTOS"))
                print("-" * 60)
                print("{:<3} {:<35} {:<12} {:<8}".format("N°", "Producto", "Categoría", "Precio"))
                print("-" * 60)

                for i, producto in enumerate(productos, 1):
                    print("{:<3} {:<35} {:<12} ${:<8}".format(i, producto[0], producto[1], producto[2]))

                pos = input("Número del producto a eliminar: ").strip()
                while not(pos.isdigit() and 1 <= int(pos) <= len(productos)):
                    print("❌ Ingresá un número válido.")
                    pos = input("Número del producto a eliminar: ").strip()

                eliminado = productos.pop(int(pos) - 1)
                print(f"🗑 Producto '{eliminado[0]}' eliminado.")

print("👋 ¡Gracias por usar el sistema de la librería!")

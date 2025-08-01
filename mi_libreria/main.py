# main.py
# libreria_crud/main.py
import clientes
import productos
from colorama import Fore, init

init(autoreset=True)

# Inicializamos base de datos (productos y categorías)
productos.inicializar_db()

# Cargamos los clientes desde el archivo JSON (opcional)
clientes_lista = clientes.cargar_clientes_json()

def menu_principal():
    print(Fore.CYAN + "\n📋 MENÚ PRINCIPAL")
    print("1. Gestionar Clientes")
    print("2. Gestionar Productos")
    print("3. Salir")

def gestionar_clientes():
    while True:
        print(Fore.MAGENTA + "\n👥 Menú Clientes")
        print("1. Agregar cliente")
        print("2. Ver clientes")
        print("3. Buscar cliente por ID")
        print("4. Eliminar cliente por ID")
        print("5. Volver al menú principal")

        opcion = input(Fore.YELLOW + "Selecciona una opción (1-5): ").strip()

        if opcion == "1":
            clientes.agregar_cliente(clientes_lista)
        elif opcion == "2":
            clientes.consultar_clientes_sql()
        elif opcion == "3":
            clientes.eliminar_cliente(clientes_lista)
        elif opcion == "4":
            clientes.eliminar_cliente_id_sql()
        elif opcion == "5":
            break
        else:
            print(Fore.RED + "❌ Opción no válida.")

def gestionar_productos():
    while True:
        print(Fore.YELLOW + "\n📦 Menú Productos")
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Buscar producto por ID")
        print("4. Actualizar producto por ID")
        print("5. Eliminar producto por ID")
        print("6. Reporte por cantidad mínima")
        print("7. Volver al menú principal")

        opcion = input(Fore.YELLOW + "Selecciona una opción (1-7): ").strip()

        if opcion == "1":
            productos.agregar_producto_sql()
        elif opcion == "2":
            productos.consultar_productos_sql()
        elif opcion == "3":
            productos.consultar_productos_sql()  # ya tiene opción por ID
        elif opcion == "4":
            productos.actualizar_producto_sql()
        elif opcion == "5":
            productos.eliminar_producto_sql()
        elif opcion == "6":
            productos.reporte_stock_bajo()
        elif opcion == "7":
            break
        else:
            print(Fore.RED + "❌ Opción no válida.")

# Menú principal
def menu_principal():
    print(Fore.GREEN + "🎉 Bienvenida al Sistema de Inventario y Gestión de Clientes 🎉")
    while True:
        print(Fore.BLUE + "\n📋 MENÚ PRINCIPAL")
        print("1. Gestionar Clientes")
        print("2. Gestionar Productos")
        print("3. Salir")

        opcion = input(Fore.YELLOW + "Selecciona una opción (1-3): ").strip()

        if opcion == "1":
            gestionar_clientes()
        elif opcion == "2":
            gestionar_productos()
        elif opcion == "3":
            print(Fore.GREEN + "👋 Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print(Fore.RED + "❌ Opción no válida. Intenta nuevamente.")

# Ejecutar la app
if __name__ == "__main__":
    menu_principal()
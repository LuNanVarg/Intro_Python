from colorama import Fore, Style, init
import productos
import clientes

init(autoreset=True)

def menu_principal():
    print(Style.BRIGHT + Fore.MAGENTA + "\n" + "=" * 40)
    print("       🛒 Menú de Tienda - CRUD       ")
    print("=" * 40)
    # print("1. Agregar producto")
    # print("2. Consultar productos")
    # print("3. Eliminar producto")
    # print("4. Salir")
    print(Fore.YELLOW + "1. Gestionar productos")
    print("2. Gestionar Clientes")
    print("3. Salir")
    print("=" * 40)

def menu_productos(): 
    print(Style.BRIGHT + Fore.MAGENTA + "----------- Menú de Productos ----")
    print("1. Agregar producto")
    print("2. Consultar productos")
    print("3. Eliminar producto")
    print("4. Volver al menú principal")

def menu_clientes():
    print(Style.BRIGHT + Fore.MAGENTA + "----------- Menú de Clientes ----")
    print("1. Agregar Clientes")
    print("2. Consultar Clientes")
    print("3. Eliminar Clientes")
    print("4. Volver al menú principal")
    
def gestionar_productos():
    while True:
        menu_productos()
        opcion = input("Selecciona una opción (1-4): ").strip()
        while not (opcion.isdigit() and 1 <= int(opcion) <= 4):
            print("❌ Opción inválida.")
            opcion = input("Selecciona una opción (1-4): ").strip()

        opcion = int(opcion)

        match opcion:
            case 1:
                productos.agregar_productos()
            case 2:
                productos.consultar_productos()
            case 3: 
                productos.eliminar_productos()
            case 4:
                break
 
def gestionar_clientes():
    while True:
        menu_clientes()
        opcion = input(Fore.YELLOW + "Selecciona una opción (1-4): ").strip()
        if opcion == '1':
            clientes.agregar_cliente()
        elif opcion == '2':
            clientes.consultar_clientes()
        elif opcion == '3':
            clientes.eliminar_cliente()
        elif opcion == '4':
            break
        else:
            print(Fore.RED + "❌ Opción inválida. Intenta nuevamente.")

# principal
def main():
        opcion = ""
        while True:
            menu_principal()
            opcion = input("Selecciona una opción (1-3): ").strip()
            while not (opcion.isdigit() and 1 <= int(opcion) <= 3):
                print("❌ Opción inválida.")
                opcion = input("Selecciona una opción (1-3): ").strip()

            opcion = int(opcion)

            match opcion:
                case 1:
                    gestionar_productos()
                case 2:
                    gestionar_clientes()
                case 3: 
                    print("👋 Saliendo del programa...")
                    break

if __name__== "__main__":
    main()
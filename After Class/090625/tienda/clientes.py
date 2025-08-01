# archivo: clientes.py
import random
from colorama import Fore, Style, init
import datetime

init(autoreset=True)

clientes = []

def validar_nombre(nombre):
    return nombre != ''

def validar_email(email):
    return "@" in email and "." in email

def agregar_cliente():
    nombre = input(Fore.YELLOW + "Ingrese nombre del cliente: ").strip().lower()
    while not validar_nombre(nombre):
        print(Fore.RED + "⚠️ Nombre inválido.")
        nombre = input(Fore.YELLOW + "Ingrese nombre válido: ").strip().lower()

    email = input(Fore.YELLOW + "Ingrese email del cliente: ").strip().lower()
    while not validar_email(email):
        print(Fore.RED + "⚠️ Email inválido.")
        email = input(Fore.YELLOW + "Ingrese email válido: ").strip().lower()

    id_cliente = random.randint(1000, 9999)
    fecha_registro = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cliente = {
        "id": id_cliente,
        "nombre": nombre,
        "email": email,
        "fecha": fecha_registro
    }
    clientes.append(cliente)
    print(Fore.GREEN + f"✅ Cliente '{nombre}' registrado con éxito (ID: {id_cliente}).")

def consultar_clientes():
    if not clientes:
        print(Fore.RED + "❌ No hay clientes disponibles.")
        return

    print(Fore.CYAN + "\n👥 Listado de clientes:")
    print("-" * 50)
    for cliente in clientes:
        print(Fore.CYAN + f"ID: {cliente['id']}")
        print(Fore.CYAN + f"Nombre: {cliente['nombre'].title()}")
        print(Fore.CYAN + f"Email: {cliente['email']}")
        print(Fore.CYAN + f"Fecha de registro: {cliente['fecha']}")
        print("-" * 50)

def eliminar_cliente():
    global clientes
    if not clientes:
        print(Fore.RED + "❌ No hay clientes para eliminar.")
        return

    nombre = input(Fore.YELLOW + "Ingrese nombre del cliente a eliminar: ").strip().lower()
    while not validar_nombre(nombre):
        print(Fore.RED + "⚠️ Nombre inválido.")
        nombre = input(Fore.YELLOW + "Ingrese nombre válido: ").strip().lower()

    cantidad_eliminados = 0
    clientes_filtrados = []
    for cliente in clientes:
        if cliente['nombre'] == nombre:
            cantidad_eliminados += 1
        else:
            clientes_filtrados.append(cliente)

    clientes = clientes_filtrados
    if cantidad_eliminados > 0:
        print(Fore.GREEN + f"🗑️ Se eliminaron {cantidad_eliminados} cliente(s) con el nombre '{nombre}'.")
    else:
        print(Fore.RED + f"❌ No se encontraron clientes con el nombre '{nombre}'.")

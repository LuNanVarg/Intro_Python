# archivo: clientes.py
import random
import json
from colorama import Fore, Style, init
import datetime

init(autoreset=True)

#clientes = [] #lista de diccionarios

def validar_nombre(nombre):
    return nombre != ''

def validar_email(email):
    return "@" in email and "." in email

def guardar_clientes_json(clientes, nombre_archivo='clientes.json'):
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as file:
            json.dump(clientes, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(Fore.RED+ "❌ Error al guardar JSON: {e}.")
        
def guardar_clientes_txt(clientes, nombre_archivo='clientes.txt'):
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as file:
            for cliente in clientes:
                #file.write(cliente)
                file.write(f"{cliente['nombre']}, {cliente['email']}\n") #falta id y fecha
    except Exception as e:
        print(Fore.RED+ "❌ Error al guardar TXT: {e}.")

def cargar_clientes_json(nombre_archivo='clientes.json'):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(Fore.RED + f"❌ Error al decodificar JSON.")
        
def agregar_cliente(clientes):
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

def consultar_clientes(clientes):
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

def eliminar_cliente(clientes):
    if not clientes:
        print(Fore.RED + "❌ No hay clientes para eliminar.")
        return

    nombre = input(Fore.YELLOW + "Ingrese nombre del cliente a eliminar: ").strip().lower()
    while not validar_nombre(nombre):
        print(Fore.RED + "⚠️ Nombre inválido.")
        nombre = input(Fore.YELLOW + "Ingrese nombre válido: ").strip().lower()
    
    #list comprehension
    # se crea la lista a partir de una secuencia existente, aplicando una condicion
    encontrados = [c for c in clientes if c['nombre'].lower() == nombre.lower()] 
    
    if not encontrados:
        print(Fore.YELLOW + "Cliente no encontrado.")
        return
    
    for cliente in encontrados:
        clientes.remove(cliente)
        
    print(Fore.GREEN + f"✔ Cliente(s) eliminados(s): {len(encontrados)}.")

        


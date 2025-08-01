# clientes.py
# libreria_crud/clientes.py
import random
# import modulo BD
import sqlite3
# import mysql.connector
import json
import os
import datetime
#from tkinter import INSERT
from colorama import Fore, init

init(autoreset=True)

#clientes = [] #lista de diccionarios
try:
    conexion = sqlite3.connect("libreria_reg.db")
    print("Conexion establecida exitosamente")
    #crear el cursor
    cursor = conexion.cursor()

    #crear tabla si no existe
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS clientes(
        cliente_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        email TEXT NOT NULL,
        fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP)
        """
    )
    print("Tabla creada existosamente.")

except sqlite3.Error as error:
    # muestra en pantalla si hubo error
    print(f"Error en la conexion a la Base de Datos: {error}")
finally:
    if conexion:
        #cierra conexion
        conexion.close()
        # retorna el estado de la transacción
        print("Conexion cerrada.")    
    
#RUTA_CLIENTES_JSON = "C:/Users/Luna/Desktop/IntroPython/mi_libreria/clientes.json"
#RUTA_CLIENTES_JSON = 'clientes.json'
#RUTA_CLIENTES_TXT = 'clientes.txt'

def validar_nombre(nombre):
    return nombre != ''

def validar_email(email):
    return "@" in email and "." in email

def cargar_clientes_json(nombre_archivo='clientes.json'):
    if not os.path.exists(nombre_archivo):
        return []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(Fore.RED + "❌ Error al decodificar JSON de clientes.")
        return []
    
def guardar_clientes_json(clientes, nombre_archivo='clientes.json'):
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as file:
            json.dump(clientes, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(Fore.RED + f"❌ Error al guardar JSON: {e}.")

def guardar_clientes_txt(clientes, nombre_archivo='clientes.txt'):
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as file:
            for cliente in clientes:
                file.write(f"{cliente['id']}, {cliente['nombre']}, {cliente['email']}, {cliente['fecha']}\n")
    except Exception as e:
        print(Fore.RED + f"❌ Error al guardar TXT: {e}.")

def agregar_cliente_sql(nombre, apellido, email, fecha_registro):
    #Ejecuta la consulta con los parametros en la lista
    conexion = sqlite3.connect("libreria_reg.db")
    cursor = conexion.cursor()
    query = "INSERT INTO clientes(nombre, apellido, email, fecha_registro) VALUES(?, ?, ?, ?)"
    #query = " INSERT INTO clientes(nombre, apellido, email, fecha_registro) VALUES('Megumi', 'Kirou', 'megumi@gmail.com', '18-06-2025')"
    cursor.execute(query, (nombre, apellido, email, fecha_registro))
    #cursor.execute("INSERT INTO clientes(nombre, apellido, email, fecha_registro) VALUES(?, ?, ?, ?)", (nombre, apellido, email, fecha_registro))
    conexion.commit()
    conexion.close()

def consultar_clientes_sql():
    conexion = sqlite3.connect("libreria_reg.db")
    cursor = conexion.cursor()
    query = "SELECT * FROM clientes"
    cursor.execute(query)
    clientes = cursor.fetchall()  #crear una lista de tuplas por registro
    conexion.close()
    
    if not clientes: 
        print(Fore.RED + "❌ No hay clientes registrados en la base de datos.")
    else:
        print(Fore.CYAN + "\n👥 Listado de clientes:")
        print("ID  | Nombre | Apellido | Email | Fecha de Registro")
        print("-" * 40)
        for cliente in clientes:
            print(Fore.CYAN + f"{cliente[0]} | {cliente[1]} | {cliente[2]} | {cliente[3]} | {cliente[4]}  ")
        
def eliminar_cliente_sql():
    nombre = input(Fore.YELLOW + "Ingrese nombre del cliente a eliminar: ").strip().lower()
    while not validar_nombre(nombre):
        print(Fore.RED + "⚠️ Nombre inválido.")
        nombre = input(Fore.YELLOW + "Ingrese nombre válido: ").strip().lower()

    conexion = sqlite3.connect("libreria_reg.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM clientes WHERE nombre = ?", (nombre,))
    conexion.commit()
    conexion.close()
    print(f"Cliente {nombre} eliminado con éxito!")

def eliminar_cliente_id_sql():
    try:
        conexion = sqlite3.connect("libreria_reg.db")
        cursor = conexion.cursor()

        #mostrar la lista de clientes => Esto se podia encapsular en una funcion
        cursor.execute("SELECT cliente_id, nombre, apellido, email FROM clientes")
        clientes = cursor.fetchall()
        if not clientes:
            print(Fore.RED + "❌ No hay clientes registrados en la base de datos.")
            return
        print("ID  | Nombre | Apellido | Email ")
        print("-" * 40)
        for cliente in clientes:
            print(Fore.CYAN + f"{cliente[0]} | {cliente[1]} | {cliente[2]} | {cliente[3]} ")
        
        #pedir el ID del cliente a eliminar
        id_cliente = input(Fore.YELLOW + "Ingrese el ID del cliente a eliminar: ").strip()
        while not id_cliente.isdigit():
            print(Fore.RED + "⚠️ ID inválido. Debe ser un número.")
            id_cliente = input(Fore.YELLOW + "Ingrese un ID válido: ").strip()

        cursor.execute("DELETE FROM clientes WHERE cliente_id = ?", (id_cliente, )) #consultar parametriza para más seguridad
        if cursor.rowcount == 0: #verifica la cantidad de filas afectadas
            print(Fore.RED + f"⚠️ No se encontró un cliente con ese ID. {id_cliente}")
        else:
            conexion.commit()
            print(Fore.GREEN + f"✅ Cliente con ID {id_cliente} eliminado con éxito.")
    except sqlite3.Error as e:
        print(Fore.RED + f"❌ Error al eliminar cliente: {e}")
    finally:
        conexion.close()

def agregar_cliente(clientes):
    nombre = input(Fore.YELLOW + "Ingrese nombre del cliente: ").strip().lower()
    while not validar_nombre(nombre):
        print(Fore.RED + "⚠️ Nombre inválido.")
        nombre = input(Fore.YELLOW + "Ingrese nombre válido: ").strip().lower()

    apellido = input(Fore.YELLOW + "Ingrese apellido del cliente: ").strip().lower()
    while not validar_nombre(apellido):
        print(Fore.RED + "⚠️ Apellido inválido.")
        apellido = input(Fore.YELLOW + "Ingrese apellido válido: ").strip().lower()

    email = input(Fore.YELLOW + "Ingrese email del cliente: ").strip().lower()
    while not validar_email(email):
        print(Fore.RED + "⚠️ Email inválido.")
        email = input(Fore.YELLOW + "Ingrese email válido: ").strip().lower()

    id_cliente = random.randint(1000, 9999)
    fecha_registro = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#Usamos otra variable para no pisar la lista 
    cliente_nuevo = {
        "id": id_cliente,
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "fecha": fecha_registro
    }
    clientes.append(cliente_nuevo)
    guardar_clientes_json(clientes)
    guardar_clientes_txt(clientes)
    print(Fore.GREEN + f"✅ Clientes '{nombre}' registrado con éxito JSON (ID: {id_cliente}).")
    agregar_cliente_sql(nombre, apellido, email, fecha_registro)
    print(Fore.GREEN + f"✅ Clientes '{nombre}' registrado con éxito SQL.")

def consultar_clientes(clientes):
    if not clientes:
        print(Fore.RED + "❌ No hay clientes disponibles.")
        return

    print(Fore.CYAN + "\n👥 Listado de clientes:")
    print("-" * 50)
    for cliente in clientes:
        print(Fore.CYAN + f"ID: {cliente['id']}")
        print(Fore.CYAN + f"Nombre: {cliente['nombre'].title()}")
        print(Fore.CYAN + f"Apellido: {cliente['apellido'].title()}")
        print(Fore.CYAN + f"Email: {cliente['email']}")
        print(Fore.CYAN + f"Fecha de registro: {cliente['fecha']}")
        print("-" * 50)
    #consultar_clientes_sql()

def eliminar_cliente(clientes):
    if not clientes:
        print(Fore.RED + "❌ No hay clientes para eliminar.")
        return

    nombre = input(Fore.YELLOW + "Ingrese nombre del cliente a eliminar: ").strip().lower()
    while not validar_nombre(nombre):
        print(Fore.RED + "⚠️ Nombre inválido.")
        nombre = input(Fore.YELLOW + "Ingrese nombre válido: ").strip().lower()

    encontrados = [c for c in clientes if c['nombre'].lower() == nombre]

    if not encontrados:
        print(Fore.YELLOW + "Cliente no encontrado.")
        return

    for cliente in encontrados:
        clientes.remove(cliente)

    guardar_clientes_json(clientes)
    guardar_clientes_txt(clientes)
    print(Fore.GREEN + f"✔ Cliente(s) eliminados(s): {len(encontrados)}.")

def actualizar_cliente_id():
    """
        Modifica un cliente en la base de datos por su ID.
    """
    try:
        conexion = sqlite3.connect("libreria_reg.db")
        cursor = conexion.cursor()

        #mostrar la lista de clientes => encapsular en una funcion
        cursor.execute("SELECT cliente_id, nombre, apellido, email FROM clientes")
        clientes = cursor.fetchall()
        if not clientes:
            print(Fore.RED + "❌ No hay clientes para actualizar.")
            return
        
        print("ID  | Nombre | Apellido | Email ")
        print("-" * 40)
        for cliente in clientes:
            print(Fore.CYAN + f"{cliente[0]} | {cliente[1]} | {cliente[2]} | {cliente[3]} ")
        
        #Pedir el ID del cliente a actualizar
        id_cliente = input(Fore.YELLOW + "Ingrese el ID del cliente a actualizar: ").strip()
        while not id_cliente.isdigit():
            print(Fore.RED + "⚠️ ID inválido. Debe ser un número.")
            id_cliente = input(Fore.YELLOW + "Ingrese un ID válido: ").strip()

        #nuevo_nombre = input("Nuevo nombre: ").strip()
        #nuevo_apellido = input("Nuevo apellido: ").strip()
        #nuevo_email = input("Nuevo email: ").strip()
        #VALIDACIONES PARA QUE LA INFORMACION SEA CORRECTO
        # Validar nombre
        nuevo_nombre = input("Nuevo nombre: ").strip().lower()
        while nuevo_nombre == '':
            print(Fore.RED + "⚠️ El nombre no puede estar vacío.")
            nuevo_nombre = input("Nuevo nombre: ").strip().lower()

        # Validar apellido
        nuevo_apellido = input("Nuevo apellido: ").strip().lower()
        while nuevo_apellido == '':
            print(Fore.RED + "⚠️ El apellido no puede estar vacío.")
            nuevo_apellido = input("Nuevo apellido: ").strip().lower()

        # Validar email
        nuevo_email = input("Nuevo email: ").strip().lower()
        while "@" not in nuevo_email or "." not in nuevo_email:
            print(Fore.RED + "⚠️ Email inválido. Debe contener '@' y '.'")
            nuevo_email = input("Nuevo email: ").strip().lower()

        cursor.execute(
            """
                UPDATE clientes
                SET nombre = ?, apellido = ?, email = ?
                WHERE cliente_id = ?
            """, (nuevo_nombre, nuevo_apellido, nuevo_email, int(id_cliente))
        )

#        query = """ UPDATE clientes SET nombre = ?, apellido = ?, email = ? WHERE cliente_id = ?"""
#        cursor.execute(query, (nuevo_nombre, nuevo_apellido, nuevo_email, id_cliente))
        
#         cursor.execute(f"""
#                UPDATE clientes
#                SET {campo_a_modificar} = ? 
#            """, (nuevo_dato))

        if cursor.rowcount == 0: #Verifica la cantidad de filas afectadas
            print(Fore.RED + f"⚠️ No se encontró un cliente con ese ID. {id_cliente}")
        else:
            conexion.commit()
            print(Fore.GREEN + f"✅ Cliente con ID {id_cliente} actualizado con éxito.")
    except sqlite3.Error as e:
        print(Fore.RED + f"Error al actualizado el cliente {e}")
    finally:
        conexion.close()
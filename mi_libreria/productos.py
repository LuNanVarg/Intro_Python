# productos.py
import sqlite3
import random
import datetime
import json
import os
from colorama import Fore, init

init(autoreset=True)

DB_PATH = "libreria_reg.db"
RUTA_PRODUCTOS_JSON = "productos.json"

# Validaciones
def validar_nombre(nombre):
    return nombre.strip() != ''

def validar_precio(precio):
    try:
        return float(precio) >=0
    except ValueError:
        return False
    
def validar_stock(stock):
    return stock.isdigit() and int(stock) >= 0

def validar_categoria(categoria_id):
    return categoria_id.isdigit()

# Backup json (opcional)
def cargar_productos_json():
    if not os.path.exists(RUTA_PRODUCTOS_JSON):
        return []
    try:
        with open(RUTA_PRODUCTOS_JSON, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(Fore.RED + "❌ Error al leer JSON de productos. Se cargará lista vacía.")
        return []

def guardar_productos_json(productos):
    try:
        with open(RUTA_PRODUCTOS_JSON, 'w', encoding='utf-8') as f:
            json.dump(productos, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(Fore.RED + f"❌ Error al guardar productos en JSON: {e}")

#Mostrar categorías disponibles
def mostrar_categoria():
    try:
        conexion = sqlite3.connect(DB_PATH)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM categorias")
        categorias = cursor.fetchall()
        if categorias:
            print(Fore.CYAN + "\n📚 Categorías disponibles:")
            for cat in categorias:
                print(Fore.CYAN + f"{cat[0]} - {cat[1]}")
        else:
            print(Fore.YELLOW + "No hay categorías registradas.")
    except sqlite3.Error as e:
        print(Fore.RED + f"Error al consultar categorías: {e}")
    finally:
        conexion.close()

# Agregar producto
def agregar_producto_sql():
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    nombre = input(Fore.YELLOW + "Ingrese nombre del producto: ").strip()
    while not validar_nombre(nombre):
        print(Fore.RED + "Nombre inválido. Ingrese solo letras.")
        nombre = input("Ingrese nombre del producto: ").strip()

    mostrar_categoria()
    categoria_id = input(Fore.YELLOW + "Seleccione ID de categoría: ").strip()
    while not categoria_id.isdigit():
        print(Fore.RED + "ID inválido. Ingrese un número.")
        categoria_id = input("Seleccione ID de categoría: ").strip()

    precio = input(Fore.YELLOW + "Precio del producto: ").strip()
    while not validar_precio(precio):
        print(Fore.RED + "Precio inválido.")
        precio = input("Precio del producto: ").strip()

    stock = input(Fore.YELLOW + "Stock disponible: ").strip()
    while not validar_stock(stock):
        print(Fore.RED + "Stock inválido.")
        stock = input("Stock disponible: ").strip()

    cursor.execute(
        "INSERT INTO productos(nombre, categoria_id, precio, stock) VALUES (?, ?, ?, ?)",
        (nombre, int(categoria_id), float(precio), int(stock))
    )
    conexion.commit()
    print(Fore.GREEN + "✅ Producto agregado con éxito.")
    conexion.close()

# Mostrar productos
def consultar_productos_sql():
    print("\n¿Querés consultar todos los productos o uno en particular?")
    print("1. Consultar todos")
    print("2. Consultar por ID")
    opcion = input("Seleccioná una opción (1-2): ")

    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    if opcion == "1":
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()

        if productos:
            for producto in productos:
                print(producto)
        else:
            print("⚠️ No hay productos cargados.")

    elif opcion == "2":
        id = input("🔎 Ingresá el ID del producto: ")
        if not id.isdigit():
            print("⚠️ ID inválido.")
        else:
            cursor.execute("SELECT * FROM productos WHERE producto_id = ?", (id,))
            producto = cursor.fetchone()
            if producto:
                print(producto)
            else:
                print("⚠️ Producto no encontrado.")

    else:
        print("⚠️ Opción inválida.")

    conexion.close()



#Eliminar producto por ID
def eliminar_producto_sql():
    id_producto = input(Fore.YELLOW + "\nID del producto a eliminar: ").strip()
    while not id_producto.isdigit():
        print(Fore.RED + "⚠️ ID inválido.")
        id_producto = input("ID del producto a eliminar: ").strip()

    try:
        conexion = sqlite3.connect(DB_PATH)
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE producto_id = ?", (id_producto,))
        if cursor.rowcount == 0:
            print(Fore.RED + f"⚠️ No se encontró producto con ID {id_producto}.")
        else:
            conexion.commit()
            print(Fore.GREEN + f"🗑️ Producto con ID {id_producto} eliminado.")
    except sqlite3.Error as e:
        print(Fore.RED + f"❌ Error al eliminar producto: {e}")
    finally:
        conexion.close()

def inicializar_db():
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categorias (
            categoria_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            producto_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria_id INTEGER,
            precio REAL,
            stock INTEGER DEFAULT 0,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id)
        )
    ''')

    categorias = ['Librería', 'Papelería', 'Regalería', 'Tecnología']
    for cat in categorias:
        cursor.execute("INSERT OR IGNORE INTO categorias (nombre) VALUES (?)", (cat,))

    conexion.commit()
    conexion.close()

def actualizar_producto_sql():
    id_producto = input("🔁 Ingresá el ID del producto a actualizar: ").strip()
    if not id_producto.isdigit():
        print(Fore.RED + "⚠️ ID inválido.")
        return

    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos WHERE producto_id = ?", (id_producto,))
    producto = cursor.fetchone()
    if not producto:
        print(Fore.RED + f"❌ No se encontró producto con ID {id_producto}.")
        conexion.close()
        return

    print(Fore.CYAN + f"Producto actual: {producto}")
    nombre = input("Nuevo nombre (Enter para mantener): ").strip() or producto[1]
    precio = input("Nuevo precio (Enter para mantener): ").strip()
    precio = float(precio) if precio else producto[3]
    stock = input("Nuevo stock (Enter para mantener): ").strip()
    stock = int(stock) if stock else producto[4]

    cursor.execute('''
        UPDATE productos
        SET nombre = ?, precio = ?, stock = ?
        WHERE producto_id = ?
    ''', (nombre, precio, stock, id_producto))
    conexion.commit()
    print(Fore.GREEN + "✅ Producto actualizado.")
    conexion.close()

def reporte_stock_bajo():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        limite = input("📉 Ingresá el límite de stock: ").strip()
        while not limite.isdigit() or int(limite) < 0:
            print("⚠️ Ingresá un número válido.")
            limite = input("📉 Ingresá el límite de stock: ").strip()

        cursor.execute('''
            SELECT p.producto_id, p.nombre, p.stock, c.nombre
            FROM productos p
            JOIN categorias c ON p.categoria_id = c.categoria_id
            WHERE p.stock <= ?
        ''', (int(limite),))

        productos = cursor.fetchall()
        if productos:
            print(f"\n📉 Productos con stock menor o igual a {limite}:")
            for prod in productos:
                print(f"ID: {prod[0]}, Nombre: {prod[1]}, Stock: {prod[2]}, Categoría: {prod[3]}")
        else:
            print("✅ No hay productos con stock por debajo del límite ingresado.")

    except Exception as e:
        print(f"❌ Error al generar el reporte: {e}")
    finally:
        conn.close()




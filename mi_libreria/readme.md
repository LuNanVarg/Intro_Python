# 🛍️ Sistema de Inventario y Gestión de Clientes

Este es un proyecto de Python con SQLite, que permite administrar clientes y productos:
agregar, modificar, eliminar y mostrar los datos almacenados en una base de datos.

## 📁 Estructura del Proyecto

```
mi_libreria/
├── clientes.py           # Lógica para gestionar clientes (alta, baja, modificación)
├── productos.py          # Lógica para gestionar productos (categorías, stock, reportes)
├── ayuda.py              # Funciones auxiliares o de utilidad (colores, validaciones, etc.)
├── main.py               # Menú principal y navegación de opciones
├── clientes.json         # Backup o precarga de datos de clientes
├── productos.json        # Backup o precarga de datos de productos
├── libreria_reg.db       # Base de datos SQLite con tablas: clientes, productos, categorias
├── README.md             # Documentación principal del proyecto (explicación general)
└── docs/                 # Documentación automática generada con Sphinx
    ├── source/
    │   ├── conf.py       # Configuración de Sphinx
    │   ├── index.rst     # Página principal de documentación
    │   └── *.rst         # Archivos adicionales generados con `sphinx-apidoc`
    └── build/            # Carpeta generada automáticamente con la salida HTML
```

## 🧰 Requisitos

- Python 3.x
- `colorama` (para colores en consola)
- SQLite (incluido en Python estándar)

## ⚙️ Instalación

1. Clona o descarga este repositorio en tu máquina local.
2. Asegúrate de tener Python 3.x instalado en tu sistema.
3. No se requieren pasos de instalación adicionales, ya que el proyecto utiliza bibliotecas estándar de Python.
4. Ejecutá el proyecto desde terminal con:
`python main.py`

## ▶️ Cómo usarlo

1. Ejecuta el archivo `main.py` para iniciar la aplicación.
2. La aplicación abrirá una ventana con las opciones disponibles.
3. La opción "Agregar producto" te permite registrar un nuevo artículo en el inventario, ingresando su nombre, precio, stock y categoría. El sistema valida los datos antes de guardarlos en la base de datos.
4. Desde la opción "Actualizar producto por ID", podés modificar el nombre, precio o stock de un producto ya registrado, utilizando su identificador único.
5. Para eliminar un producto del sistema, accedé a la opción "Eliminar producto por ID", donde se te solicitará el ID del producto a borrar.
6. La opción "Reporte por cantidad mínima" permite ingresar un límite de stock. El sistema mostrará un listado con todos los productos cuyo stock sea menor o igual al número ingresado, incluyendo su ID, nombre y categoría.

## Lógica de Funcionamiento

1. `main.py`
*  Presenta el menú principal con opciones para Clientes, Productos o Salir.
*  Redirige al módulo correspondiente usando match.

2. 👥 `clientes.py`
**Funciones:**
* `agregar_cliente_sql()`: Alta en BD.
* `ver_clientes_sql()`: Muestra clientes.
* `buscar_cliente_por_id()`
* `eliminar_cliente_por_id()`

**Validaciones:**
* Campos obligatorios.
* Email válido.
* Fecha con `datetime`.

📦 `productos.py`
**Funciones:**
* `agregar_producto_sql()`
* `consultar_productos_sql()`
* `buscar_producto_por_id()`
* `actualizar_producto_sql()`
* `eliminar_producto_sql()`
* `reporte_stock_bajo()`
**Validaciones:**
Precio y stock positivos.
Categoría existente.

## 💾Base de Datos
Archivo: `libreria_reg.db`
```
-- clientes
CREATE TABLE IF NOT EXISTS clientes (
    cliente_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    fecha_registro TEXT NOT NULL
);

-- productos
CREATE TABLE IF NOT EXISTS productos (
    producto_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    stock INTEGER NOT NULL,
    categoria_id INTEGER,
    FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id)
);

-- categorias
CREATE TABLE IF NOT EXISTS categorias (
    categoria_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
);
```

## Ejemplo de Uso
### 📋 MENÚ PRINCIPAL
1. Gestionar Clientes
2. Gestionar Productos
3. Salir
Selecciona una opción (1-3): 2

### 📦 Menú Productos
1. Agregar producto
2. Ver productos
...
6. Reporte por cantidad mínima
Selecciona una opción (1-7): 6
📉 Ingresá el límite de stock: 5
➡️ Muestra todos los productos con stock menor o igual a 5

## 🐞 Errores Comunes 

|    Error           |    Causa               |       Solución                       |
| -------------------| -----------------------| ------------------------------------ |
| `AttributeError:`  | Nombre de función mal  | Revisar nombres exactos              |
|  `module has no`   | llamado.               |  en el archivo py                    |
|  `attribute`       |                        |                                      |
| -------------------|-------------------     |------------------------------------- |
| `sqlite3.Operation`| El alias o nombre de   | Verificar nombres reales en la       |
| `alError: no such` | columna/tablas         | base de datos                        |
| `column`           |                        |                                      |
|------------------- |------------------------|------------------------------------- |


## ✅ Mejoras futuras

- Agregar interfaz gráfica (Tkinter o PyQt).
- Conexión con API REST.
- Exportar reportes a CSV o Excel.

## 🔎 Consideraciones

- Se usa `init(autoreset=True)` para usar `colorama` en la consola.
- Los datos también pueden persistirse en archivo `.json` como respaldo externo.
- Se incorporan íconos en consola para mejor experiencia (como ✅, ❌, 📢).

## 🙌 Agradecimientos

Quiero agradecer especialmente a la profesora Griselda por su dedicación y guía constante a lo largo del curso, y a la tutora Erica, por su acompañamiento atento y paciente en cada consulta.
Este proyecto fue realizado como parte de mi formación en el curso de Python. Cada línea de código representa horas de práctica, errores y aprendizajes que hoy forman parte de mi crecimiento en el mundo de la programación.




# 🐍 Iniciación con Python - Talento Tech

Este repositorio contiene ejercicios, prácticas y un proyecto final desarrollados a lo largo del curso inicial con Python de la comisión 25009. Cada archivo y carpeta refleja el proceso de aprendizaje, la resolución de problemas y la aplicación progresiva de conceptos clave de la programación. 

---
## 📚 Temas Principales

- 🐍 Fundamentos de Python: variables, tipos de datos, operadores
- 🔁 Control de flujo: `if`, `for`, `while`
- 📋 Estructuras de datos: listas, diccionarios, tuplas, cadenas
- 🧩 Funciones y modularización
- 🗃️ Archivos JSON y persistencia de datos
- 🛢️ Introducción a bases de datos relacionales (SQLite)
- 🚀 Proyecto integrador final

---

## ✅ Estructura del aprendizaje 
```
Intro_Python/
│
├── 🐍 Fundamentos de Programación
│   ├── Concepto de algoritmo
│   ├── Entrada / Proceso / Salida
│   ├── Variables y tipos de datos
│   └── Operadores
│
├── 🔁 Estructuras de Control
│   ├── Condicionales (if, elif, else, match)
│   ├── Bucles (while, for)
│   ├── Acumuladores y contadores
│   └── Uso de break y continue
│
├── 📋 Estructuras de Datos
│   ├── Cadenas
│   ├── Listas
│   ├── Tuplas
│   └── Diccionarios
│
├── 🧩 Funciones y Modularización
│   ├── Definición de funciones
│   ├── Parámetros y retorno
│   ├── Alcance de variables
│   └── División del código en módulos
│
├── 💾 Archivos y Persistencia
│   ├── Manejo de archivos .txt
│   ├── Uso de archivos .json
│   ├── Estructuras de datos persistentes
│   └── Manejo de errores (try-except)
│
├── 🗃️ Bases de Datos y SQL
│   ├── Introducción a SQLite
│   ├── Conexión desde Python
│   ├── Consultas SQL básicas (CRUD)
│   └── Integración con estructuras Python
│
└── 🚀 Proyecto Final Integrador
    ├── Desarrollo de aplicación en consola
    ├── Gestión de productos y clientes
    ├── Uso de archivos y base de datos
    └── Documentación y presentación

```

---

## 🧰 Herramientas y tecnologías utilizadas

<p align="center">
  &emsp;
  <a href="#"><img alt="Python" src="https://img.shields.io/badge/Python-3776AB.svg?style=plastic&logo=python&logoColor=white"></a>
  &emsp;
  <a href="#"><img alt="SQLite" src="https://img.shields.io/badge/SQLite-07405E.svg?style=plastic&logo=sqlite&logoColor=white"></a>
  &emsp;
  <a href="#"><img alt="JSON" src="https://img.shields.io/badge/JSON-000000.svg?style=plastic&logo=json&logoColor=white"></a>
  &emsp;
  <a href="#"><img alt="Visual Studio Code" src="https://img.shields.io/badge/VSCode-0078d7.svg?style=plastic&logo=visual-studio-code&logoColor=white"></a>
  &emsp;
  <a href="#"><img alt="Git" src="https://img.shields.io/badge/Git-F05033.svg?style=plastic&logo=git&logoColor=white"></a>
  &emsp;
  <a href="#"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-181717.svg?style=plastic&logo=github&logoColor=white"></a>
  &emsp;
  <a href="#"><img alt="Colorama" src="https://img.shields.io/badge/Colorama-FFD43B.svg?style=plastic&logo=python&logoColor=black"></a>
</p>

---

## ⚙️ Funcionalidades

Este proyecto fue desarrollado utilizando diversas herramientas y tecnologías:

- 🐍 **Python**: lenguaje principal del proyecto  
- 💾 **SQLite**: base de datos relacional utilizada para la gestión de productos  
- 📂 **JSON**: para la persistencia de datos de clientes  
- 🎨 **Colorama**: librería usada para agregar colores en la interfaz de consola  
- 🧰 **Visual Studio Code**: editor de código principal utilizado durante el desarrollo  
- 🔧 **Git y GitHub**: para control de versiones y colaboración

**Funcionalidades implementadas:**

- 📦 Gestión de productos con SQLite  
- 👥 Gestión de clientes con archivo JSON  
- 🧩 Menús interactivos por consola  
- ✅ Validaciones de entrada  
- 🎨 Interfaz con colores (Colorama)  
- 📁 Separación en módulos, ejemplos:(`clientes.py`, `productos.py`, `main.py`)

Además, incorporamos **Sphinx** como herramienta para documentar el proyecto:

- 📚 `Sphinx`: Generador de documentación automática para proyectos en Python
- 🗂️ `.rst` y `conf.py`: Archivos fuente de la documentación
- 🌐 `HTML`: Generación de documentación navegable en `docs/build/html`

**La estructura generada incluye:**

```
docs/
├── build/          ← Documentación HTML generada
├── source/         ← Archivos fuente (.rst, conf.py)
├── index.rst       ← Archivo principal de la documentación
├── conf.py         ← Configuración de Sphinx
├── Makefile        ← Script para generar HTML (Linux/macOS)
└── make.bat        ← Script para generar HTML (Windows)
```

**Para compilar la documentación:**
```
cd docs
make html  # o make.bat html en Windows
```
---

## ▶️ Cómo ejecutar

**1. Cloná el repositorio:**

``` bash
git clone https://github.com/LuNanVarg/Intro_Python.git
cd Intro_Python
```
**2. Ejecutá el archivo principal:**
   ```python main.py```

---
## 💾 Requisitos

* Python 3.11 o superior
* Módulos externos:
    * ```colorama```

**Instalación:**

```pip install colorama```

---
## 📌 Notas

* Este proyecto forma parte de mi formación práctica en Python.
* Fue realizado con el objetivo de integrar archivos JSON, SQL y estructuras de control.
* Cada función fue probada y mejorada durante el proceso de aprendizaje, clase a clase .
* Organizado en carpetas para facilitar la lectura y presentación.

---
## 🙌 Agradecimientos

Gracias al equipo docente **( profe Griselda y a la tutora Erica)** y a mis compañeros del curso por acompañarme en este camino.
Cada línea de código representa horas de práctica, errores y aprendizajes que hoy forman parte de mi crecimiento en el mundo de la programación.
Este proyecto es también un reflejo de mi compromiso con seguir aprendiendo y superándome.

---

## <img src="https://github.com/7oSkaaa/7oSkaaa/blob/main/Images/Connect-with-me.gif?raw=true" width="100px"> </picture> 👩‍💻 Autor
<p align="center">
	<a href="mailto:nancy.vargas.it@gmail.com"><img src="https://img.icons8.com/bubbles/50/000000/gmail.png" alt="Gmail"/></a>
	<a href="https://github.com/LuNanVarg"><img src="https://img.icons8.com/bubbles/50/000000/github.png" alt="GitHub"/></a>
	<a href="https://linkedin.com/in/vargasnancy"><img src="https://img.icons8.com/bubbles/50/000000/linkedin.png" alt="LinkedIn"/></a>
	
</p>

---

## 🚀 En desarrollo

* ✍️ Validaciones más robustas
* 📊 Reportes personalizados
* 🌐 Versión con interfaz gráfica (próximamente)
  
---

## 🛠️ Próximos pasos

- Explorar Python orientado a objetos
- Probar frameworks como Flask o Tkinter
- Conectar Python con interfaces gráficas y web

---

## 🏁 Resultados de Aprendizaje

Al finalizar el curso, ya somos capaces de:

* ✅ Escribir y ejecutar programas simples en Python

* ✅ Aplicar estructuras de control para decisiones y repeticiones

* ✅ Dividir tareas complejas usando funciones propias

* ✅ Utilizar buenas prácticas de programación (modularidad, depuración, mantenibilidad)

* ✅ Manipular datos con listas, diccionarios y bases de datos SQLite

* ✅ Crear y gestionar bases de datos con SQL básico

* ✅ Desarrollar pequeñas aplicaciones prácticas integrando todo lo aprendido

💡 El curso culminó con un proyecto integrador, demostrando una base sólida para continuar formándonos en programación y desarrollo de software.

---

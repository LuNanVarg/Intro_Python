#test.py

mi_variable = 'cuestionario 2'
print(type(mi_variable))
mi_variable = 2
print(type(mi_variable))

_otra_variable = 'dos' #no es recomendable para las variables
print(type(_otra_variable))

#edad = int(input("Ingrese su edad: "))
print("Producto:\tManzanas\n Precio:\t$1.00")

print(bool(0))

#asignacion multiple
x, y, z = 1, 2, 3

print(x + y + z) #6

#division entera
resultado = 7 // 3
print(resultado) #int
#division 
resultado = 7 / 3
print(resultado) #float

x, y, z = input("x: "), input("y: "), input("z: ")
print(x, y ,z )

#nombre-completo #error
#1nombre
NombreCompleto = "Rosa Mesa" #no es buena práctica

# estructura básica del programa (CRUD - Create, Read, Update, Delete)
# menú ejemplo
print("=" * 40)
print("       🛒 Menú de Tienda - CRUD       ")
print("=" * 40)
print("1. Agregar producto")
print("2. Ver productos")
print("3. Actualizar producto")
print("4. Eliminar producto")
print("5. Salir")
print("=" * 40)
opcion = int(input("Selecciona una opción (1-5): "))
print("Seleccionaste: ", opcion)
input("\nPresiona Enter para continuar...\n")
# variables, condicionales, validar datos de entrada
## validar opción válida de menú por ejemplo
# interfaces de usuario

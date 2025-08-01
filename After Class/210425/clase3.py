# estructura básica del programa (CRUD - Create, Read, Update, Delete)
# menú ejemplo
print("=" * 40)
print("       🛒 Menú de Tienda - CRUD       ")
print("=" * 40)
print("1. Agregar cliente")
print("2. Ver clientes")
print("3. Actualizar cliente")
print("4. Eliminar cliente")
print("5. Salir")
print("=" * 40)

opcion = int(input("Selecciona una opción (1-5): "))
print("Seleccionaste: ", opcion)
input("\nPresiona Enter para continuar...\n")

if opcion == 1: 
    #agregar cliente
    print("======== Registro de cliente ============")

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    correo = input("Ingrese su correo: ")

    #validación básica con los mensajes de error por camino de falsedad (else)
    if len(nombre) != 0 and len(apellido) != 0 and len(correo) != 0 and len(edad) != 0: # funcion len devuelve la cantidad de caracteres del input 
    #if nombre != '' and apellido != '' and correo != '' and edad != '':
        if edad.isdigit(): #metodo que retorna true o false, dependiendo si el string es numerico
            edad = int(edad)
            if edad > 18:
                #informamos los datos ingresados
                print(f"Nombre: {nombre.title()}")
                print(f"Apellido: {apellido.title()}")
                print(f"Edad: {edad}")
                print(f"Correo: {correo.lower()}")
            else:
                print("❌ Error! edad no válida!")
        else:
            print("❌ Error!: edad no numérica")

    else:
        #preferentemente los msjs de error
        print("❌ Error! Datos ingresados vacíos")
        
        
    #otra alternativa
    # if nombre == '' or apellido == '' or correo == '' or edad == '':
    #     print("❌ Error! Datos ingresados vacíos")
    # else:
    #     if edad.isdigit(): #metodo que retorna true o false, dependiendo si el string es numerico
    #         edad = int(edad)
    #         print("Ok")
    #     else:
    #         print("❌ Error en edad!")
    
elif opcion == 2:
    print("Ver Cliente")
elif opcion == 3:
    print("Actualizar cliente")
elif opcion == 4:
    print("Eliminar cliente")
elif opcion == 5:
    print("Saliendo del sistema!...")
else:
    print("Opción Inválida!")
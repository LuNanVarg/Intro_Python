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

opcion = input("Selecciona una opción (1-5): ") #validar de que sea entero
#validamos que sea nro y entre 1 y 5
while not(opcion.isdigit() and 1 <= int(opcion) <= 5):
    print("❌ Opción Ínválida!")
    opcion = input("Selecciona una opción (1-5): ")
    
opcion = int(opcion)

print("Seleccionaste: ", opcion)
    #input("\nPresiona Enter para continuar...\n")
while opcion != 5:
    #opciones del menú
    match opcion:
        case 1: 
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
                    
                    if correo.count("@") == 1 and " " not in correo:
                        #informamos los datos ingresados
                        print(f"Nombre: {nombre.strip().title()}") #coloca la primera letra en mayus y el resto en minus
                        print(f"Apellido: {apellido.strip().title()}")
                        print(f"Edad: {edad}")
                        correo = correo.strip().lower() 
                        # antes de reemplazar verificar que la subcadena se encuentre dentro de la cadena
                        correo.replace("@gmail.com", "@miempresa.com")
                        # verificar si termina con una extension particular
                        if correo.endswith(".com"):
                            print("finaliza en .com")
                            
                        print(f"Correo: {correo}") #coloca todo en minusc
                        
                        #clasificar por rango etario
                        if edad < 15:
                            print("Clasificación: Niño/a")
                        elif edad <= 18:
                            print("Clasificación: Adolescente")
                        else:
                            print("Clasificación: Adulto")
                        
                        mes = 1 #contador
                        suma_ingresos = 0.0 #acumulador
                        ingresos = [] #lista
                        while mes <= 6:
                            # solicitamos ingreso
                            ingreso_str = input(f"Ingreso del mes {mes}: ").strip()
                            # validamos que sea numérico - flotante
                            # 12.3 -> 123
                            # 5876.63 -> 587663
                            if not ingreso_str.replace(".", '', 1).isdigit():
                                print("Valor inválido, ingrese un numéro")
                                continue
                            ingreso = float(ingreso_str)
                            # validamos valor no sea negativo
                            if ingreso < 0:
                                print("Valor inválido!")
                                continue
                            # acumulamos en suma_ingresos
                            suma_ingresos += ingreso
                            ingresos.append(ingreso) #agrego item a la lista
                            mes += 1 

                        #imprimo resultados y lista creada
                        for item in ingresos:
                            print(item)
                        print(suma_ingresos) #usar máscara para los decimales o la función round()

                           
                        
                    else:
                        print("❌ Error!: mail no válido")
                else:
                    print("❌ Error!: edad no numérica")

            else:
                #preferentemente los msjs de error
                print("❌ Error! Datos ingresados vacíos")
                
        case 2:
            print("Ver Cliente")
        case 3:
            print("Actualizar cliente")
        case 4:
            print("Eliminar cliente")
        case _:
            print("Opción Inválida!")
            
    print("=" * 40)
    print("       🛒 Menú de Tienda - CRUD       ")
    print("=" * 40)
    print("1. Agregar cliente")
    print("2. Ver clientes")
    print("3. Actualizar cliente")
    print("4. Eliminar cliente")
    print("5. Salir")
    print("=" * 40)

    opcion = int(input("Selecciona una opción (1-5): ")) #validar de que sea entero
    print("Seleccionaste: ", opcion)
    #validamos que sea nro y entre 1 y 5
    while not(opcion.isdigit() and 1 <= int(opcion) <= 5):
        print("❌ Opción Ínválida!")
        opcion = input("Selecciona una opción (1-5): ")
    
    if opcion == 5:
        print("Saliendo del sistema...")
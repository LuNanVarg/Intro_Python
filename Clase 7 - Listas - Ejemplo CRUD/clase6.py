clientes = []

clientes = [
    ["José", "Gómez", 35, "jgomez@gmail.com"],
    ["Rosa", "Mesa", 60, "rmesa@gmail.com"],
    ["Luis", "Ojeda", 50, "lgg@gmail.com"],
    ["Luis", "Perez", 40, "lgg@gmail.com"]  
]
#Visualización de clientes
#print("======== Visualización de clientes ============")
#if clientes:
    #pass #Se utiliza pero con print, siempre separados, se utiliza cuando falta algo. 
#else:
    #print("No hay clientes registrados")
    
# menú ejemplo
print("=" * 40)
print("       🛒 Menú de Tienda - CRUD       ")
print("=" * 40)
print("1. Agregar cliente")
print("2. Ver clientes")
print("3. Actualizar cliente")
print("4. Buscar cliente")
print("5. Eliminar cliente")
print("6. Salir")
print("=" * 40)

opcion = input("Selecciona una opción (1-6): ") #validar de que sea entero
#validamos que sea nro y entre 1 y 5
while not(opcion.isdigit() and 1 <= int(opcion) <= 6):
    print("❌ Opción Ínválida!")
    opcion = input("Selecciona una opción (1-6): ")
    
opcion = int(opcion)

while opcion != 6:
    #opciones del menú
    match opcion:
        case 1: 
            # Registro de clientes agregar cliente
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
                        nombre_formateado = nombre.strip().title()
                        apellido_formateado = apellido.strip().title()
                        correo_formateado = correo.strip().lower() 
                        print(f"Nombre: {nombre_formateado}") #coloca la primera letra en mayus y el resto en minus
                        print(f"Apellido: {apellido_formateado}")
                        print(f"Edad: {edad}")
                        print(f"Correo: {correo_formateado}") #coloca todo en minusc
                        cliente = [nombre_formateado, apellido_formateado, edad, correo_formateado]
                        clientes.append(cliente)
                        print("✔ Cliente Registrado")
            
        case 2:
            
            # Visualización de clientes
            print("======== Visualización de clientes ============")
            if not clientes:
                print("❌ No hay clientes registrados.")
            else:
                print("💬 Lista de Clientes: ")
                for i, cliente in enumerate(clientes, 1):
                    # nombre, apellido, edad, correo = cliente
                    # print(f"{i}. {nombre} {apellido} - Edad: {edad} - Correo {correo}")
                    # otra forma:
                    print(f"{i}. {cliente[0]} {cliente[1]} - Edad: {cliente[2]} - Correo {cliente[3]}")
                    
        case 3:
            pass
        case 4: 
            # busqueda de clientes
            print("======== Búsqueda de clientes ============")
            if not clientes:
                print("❌ No hay clientes registrados.")
            else:
                busqueda = input("🔍 Ingrese el nombre a buscar: ").strip().title()
                encontrados = []
                
                for cliente in clientes:
                    if cliente[0] == busqueda:
                        encontrados.append(cliente)
                        
                if encontrados:
                    print("📝 Resultados encontrados: ")
                    for i, cliente in enumerate(encontrados, 1):
                        nombre, apellido, edad, correo = cliente
                        print(f"{i}. {nombre} {apellido} - Edad: {edad} - Correo {correo}")
                        # otra forma:
                        # print(f"{i}. {cliente[0]} {cliente[1]} - Edad: {cliente[2]} - Correo {cliente[3]}")
                else:
                    print(f"❌No se encontraron resultados con nombre: {busqueda}")
        case 5:           
            #eliminación 
            if not clientes: 
                print("❌ No hay clientes registrados.")
            else:
                print("💬 Lista de Clientes: ")
                for i, cliente in enumerate(clientes, 1):
                    # nombre, apellido, edad, correo = cliente
                    # print(f"{i}. {nombre} {apellido} - Edad: {edad} - Correo {correo}")
                    # otra forma:
                    print(f"{i}. {cliente[0]} {cliente[1]} - Edad: {cliente[2]} - Correo {cliente[3]}")
                
                posicion = input("Ingrese el número de cliente a eliminar: ").strip()
                while not posicion.isdigit() or int(posicion) < 1 or int(posicion) > len(clientes):
                    print("Ingrese valor válido: ")
                    posicion = input("Ingrese el número de cliente a eliminar: ").strip()
                    
                pos = int(posicion)
                
                #dentro del rango de mi lista
                cliente_eliminado = clientes.pop(pos - 1)
                print(f"🗑 Cliente {cliente_eliminado[0]} {cliente_eliminado[1]} eliminado.")
        

    print("=" * 40)
    print("       🛒 Menú de Tienda - CRUD       ")
    print("=" * 40)
    print("1. Agregar cliente")
    print("2. Ver clientes")
    print("3. Actualizar cliente")
    print("4. Buscar cliente")
    print("5. Eliminar cliente")
    print("6. Salir")
    print("=" * 40)

    opcion = input("Selecciona una opción (1-5): ") #validar de que sea entero
    #validamos que sea nro y entre 1 y 5
    while not(opcion.isdigit() and 1 <= int(opcion) <= 6):
        print("❌ Opción Ínválida!")
        opcion = input("Selecciona una opción (1-5): ")
        
    opcion = int(opcion)
    

print("Saliendo...")           
# 
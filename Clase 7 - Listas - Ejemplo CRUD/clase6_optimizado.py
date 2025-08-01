## inciiar desde lista vacía
#clientes = []

clientes = [
    ["José", "Gómez", 35, "jgomez@gmail.com"],
    ["Rosa", "Mesa", 60, "rmesa@gmail.com"],
    ["Luis", "Ojeda", 50, "lgg@gmail.com"],
    ["Luis", "Perez", 40, "lgg@gmail.com"]  
]

# Menú principal
opcion = ""
while opcion != 6:
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

    opcion = input("Selecciona una opción (1-6): ").strip()
    while not (opcion.isdigit() and 1 <= int(opcion) <= 6):
        print("❌ Opción inválida.")
        opcion = input("Selecciona una opción (1-6): ").strip()

    opcion = int(opcion)

    match opcion:
        case 1:
            print("======== Registro de cliente ============")

            nombre = input("Ingrese su nombre: ").strip()
            apellido = input("Ingrese su apellido: ").strip()
            edad = input("Ingrese su edad: ").strip()
            correo = input("Ingrese su correo: ").strip()

            # validaciones con variable bandera, alternativa al while
            datos_ok = True  # bandera

            if not nombre or not apellido or not edad or not correo:
                print("❌ Todos los campos son obligatorios.")
                datos_ok = False

            if datos_ok and not edad.isdigit():
                print("❌ La edad debe ser un número.")
                datos_ok = False
            else:
                edad = int(edad)

            if datos_ok and (correo.count("@") != 1 or " " in correo):
                print("❌ El correo no es válido.")
                datos_ok = False

            if datos_ok:
                cliente = [
                    nombre.title(),
                    apellido.title(),
                    edad,
                    correo.lower()
                ]
                clientes.append(cliente)
                print("✔ Cliente registrado exitosamente.")
            else:
                print("❌ Algún dato es inválido.")

        case 2:
            print("======== Lista de clientes ============")
            if not clientes:
                print("❌ No hay clientes registrados.")
            else:
                print("\n📋 {:^60}".format("LISTADO DE CLIENTES"))
                print("-" * 60)
                print("{:<3} {:<15} {:<15} {:<5} {:<25}".format("N°", "Nombre", "Apellido", "Edad", "Correo"))
                print("-" * 60)

                for i, cliente in enumerate(clientes, 1):
                    print("{:<3} {:<15} {:<15} {:<5} {:<25}".format(i, cliente[0], cliente[1], cliente[2], cliente[3]))

        case 3:
            pass

        case 4:
            print("======== Búsqueda de cliente ============")
            if not clientes:
                print("❌ No hay clientes registrados.")
            else:
                nombre_buscar = input("🔍 Ingrese el nombre a buscar: ").strip().title()
                encontrados = [c for c in clientes if c[0] == nombre_buscar]

                if encontrados:
                    print("📝 Resultados encontrados:")
                    print("-" * 60)
                    print("{:<3} {:<15} {:<15} {:<5} {:<25}".format("N°", "Nombre", "Apellido", "Edad", "Correo"))
                    print("-" * 60)

                    for i, cliente in enumerate(encontrados, 1):
                        print("{:<3} {:<15} {:<15} {:<5} {:<25}".format(i, cliente[0], cliente[1], cliente[2], cliente[3]))
                else:
                    print(f"❌ No se encontraron clientes con el nombre: {nombre_buscar}")

        case 5:
            print("======== Eliminación de cliente ============")
            if not clientes:
                print("❌ No hay clientes registrados.")
            else:
                print("\n📋 {:^60}".format("LISTADO DE CLIENTES"))
                print("-" * 60)
                print("{:<3} {:<15} {:<15} {:<5} {:<25}".format("N°", "Nombre", "Apellido", "Edad", "Correo"))
                print("-" * 60)

                for i, cliente in enumerate(clientes, 1):
                    print("{:<3} {:<15} {:<15} {:<5} {:<25}".format(i, cliente[0], cliente[1], cliente[2], cliente[3]))

                pos = input("Ingrese el número de cliente a eliminar: ").strip()
                while not (pos.isdigit() and 1 <= int(pos) <= len(clientes)):
                    print("❌ Número inválido.")
                    pos = input("Ingrese el número de cliente a eliminar: ").strip()

                eliminado = clientes.pop(int(pos) - 1)
                print(f"🗑 Cliente {eliminado[0]} {eliminado[1]} eliminado.")

print("👋 Saliendo del sistema...")


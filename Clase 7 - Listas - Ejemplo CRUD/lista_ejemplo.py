clientes = [
    ["José", "Gómez", 35, "jgomez@gmail.com"],
    ["Rosa", "Mesa", 60, "rmesa@gmail.com"],
    ["Luis", "Ojeda", 50, "lgg@gmail.com"],
    ["Luis", "Perez", 40, "lgg@gmail.com"]  
       
]

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
        
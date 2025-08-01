#funciones sin parametros y con retorno de valor
def obtener_nombre_formateado():
    '''
    Retorno el nombre completo con algún formato
    '''
    nombre = input("Ingrese nombre: ")
    apellido = input("Apellido")
    segundo_nombre = input("Segundo Nombre: ")
    if segundo_nombre != '':
        nombre_completo = nombre.title()+' '+segundo_nombre.title()+' '+apellido.title()
    else:
        nombre_completo = nombre.title()+' '+apellido.title()
        
    return nombre_completo


#main
persona = obtener_nombre_formateado()
print(persona)
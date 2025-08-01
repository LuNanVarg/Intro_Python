# nombre_formateado3.py
# Esta es la mejor manera de trabajarlo
# Funcion sin parámetros y con retorno de valores
def obtener_nombre_formateado():
    '''
    Retorna el nombre completo con algún formato.
    '''
    nombre = input("Ingrese nombre: ")
    apellido = input("Apellido: ")
    segundo_nombre = input("Ingrese segundo nombre (opcional): ")
    if segundo_nombre != '':
        nombre_completo = nombre.title()+' '+segundo_nombre.title()+' '+apellido.title()
    else:
        nombre_completo = nombre.title()+' '+apellido.title()
    return nombre_completo

#main
persona = obtener_nombre_formateado()
print(persona)

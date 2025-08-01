#nombre_formateado2.py
# Funcion con parámetros y retorno de valores
def obtener_nombre_formateado(nombre, apellido, segundo_nombre = ''):
    '''
    Retorna el nombre completo con algún formato.
    '''
    if segundo_nombre != '':
        nombre_completo = nombre.title()+' '+segundo_nombre.title()+' '+apellido.title()
    else:
        nombre_completo = nombre.title()+' '+apellido.title()

    return nombre_completo

#Principal
musico = obtener_nombre_formateado('jimi', 'hendrix')
print(musico)
actor = obtener_nombre_formateado('tomy','jones', 'lee')
print(actor)

name = input("Ingrese nombre: ")
last_name = input("Apellido: ")
persona = obtener_nombre_formateado(name, last_name)
print(persona)



#nombre_formateado.py
# Función con parámetros y retorno de valores
def obtener_nombre_formateado(nombre, apellido):
    '''
    Retorno el nombre completo con algún formato
    '''
    nombre_completo = nombre.title()+' '+apellido.title()
    return nombre_completo

#principal
musico = obtener_nombre_formateado('jimi', 'hendrix')
print(musico)
nombre_input = 'jane'
apellido_input = 'fonda'
actriz = obtener_nombre_formateado('jane', 'fonda')
print(actriz)
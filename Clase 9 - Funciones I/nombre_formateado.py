#nombre_formateado.py

def obtener_nombre_formateado(nombre, apellido):
    '''
    Retorna el nombre y apellido completo con algún formato.
    '''
    nombre_completo = nombre.title() + ' ' + apellido.title()
    return nombre_completo

#Principal
musico = obtener_nombre_formateado('Jimi', 'Hendrix')
print(musico)
nombre_input = 'Jane'
apellido_input = 'Fonda'
actriz = obtener_nombre_formateado('jame', 'fonda')
print(actriz)
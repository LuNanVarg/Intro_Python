#usando argumentos arbitrarios clave valor
def crear_perfil(nombre, apellido, **info_usuario): #argumento es diccionario
    '''
    Crear un diccionario que contiene toda la info del usuario
    '''
    perfil = {}
    perfil['nombre'] = nombre
    perfil['apellido'] = apellido
    for clave, valor in info_usuario.items():
        perfil[clave] = valor
        
    return perfil

#main
perfil_usuario = crear_perfil('albert', 'einstein', ubicacion = 'princeton', area = 'física', edad = '78')
#print(perfil_usuario)
for k, v in perfil_usuario.items():
    print(f"{k} : {v}")
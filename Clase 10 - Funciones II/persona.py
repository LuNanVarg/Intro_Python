#retornando diccionario
def crear_persona(nombre, apellido, edad=''):
    '''
    Retorna un diccionario con la información de una persona
    '''
    persona = {'nombre': nombre, 'apellido': apellido}
    if edad != '':
        persona['edad'] = edad
    return persona

#main
modelo = crear_persona('wanda', 'nara') #diccionario
print(modelo)
musico = crear_persona('jimmi', 'hendrix', edad=27)
print(musico)

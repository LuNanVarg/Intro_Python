# Retornando diccionario
def crear_persona (nombre, apellido):
    '''
    Retorna un diccionario con la información de una persona.
    '''
    persona = {'nombre': nombre, 'apellido': apellido}
    if edad != '': # Solo si edad tiene algún valor
        persona['edad'] = edad
    return persona



#Main
modelo = crear_persona('wanda', 'nara') #diccionario
print(modelo)
musico = crear_persona('jimi', 'hendriz', edad=27)
print(musico)

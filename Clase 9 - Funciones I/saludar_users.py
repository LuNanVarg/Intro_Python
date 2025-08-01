#pasando una lista
def saludar_usuarios(names):
    '''
    Imprime un saludo a cada nombre de la lista
    '''
    for name in names:
        print(f"Hola {name.title()}, bienvenido!")

#main
#lista
usuarios = []
while True:
    print("Lista de ususarios - Fin para salir")
    usuario = input('Nombre de user: ')
    usuarios.append(usuario)
    if usuario.title() == 'Fin': 
        break
    saludar_usuarios(usuarios) #lista como argumento

#saludar_usuarios(['josé', 'Martina', 'Roxi']) #lista como argumento

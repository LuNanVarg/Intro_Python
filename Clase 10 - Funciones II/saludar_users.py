#pasando una lista
def saludar_usuarios(names):
    '''
    Imprime un saludo a cada nombre de la lista
    '''
    for name in names:
        print(f"Hola {name.title()}, bienvenido!")
        
#main
usuarios = []
while True:
    print("Lista de usuarios - Fin para salir")
    usuario = input('Nombre de user: ')
    usuarios.append(usuario)
    if usuario.title() == 'Fin': #corregir para que no guarde el user Fin
        break
saludar_usuarios(usuarios) #lista como argumento
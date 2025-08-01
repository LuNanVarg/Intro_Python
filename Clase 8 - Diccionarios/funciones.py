"""
#funciones.py
"""
#Definir un simple funcion
def saludar(username): #parámetro
    '''
    muestra un simple saludo personalizado
    '''
    print(f"Hola {username.title()}, como estas?")

#Principal
print("Encabezado...  ")
#invocar la funcion con el argumento
user = input("Ingrese su username: ")
saludar(user) #pasando info por referencia
saludar("Ramón") #pasando info por valor
print("Continua la ejecución... ")


#Fin 
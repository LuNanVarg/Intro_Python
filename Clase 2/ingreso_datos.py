
#ingreso_datos.py
# los datos ingresados por teclado si o si son string
'''
Entrada
'''
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
# str -> int
# forma abreviada
edad = int(input("Edad: "))
# forma extensa
# edad = input("Edad: ")
# edad = int(edad)
#str -> float
altura = float(input("Altura: "))
peso = float(input("Peso: "))
'''
Proceso
'''
imc = peso/altura**2
#round(imc,2)
'''
Salida
'''
print("Hola: ", apellido, end=", ") #concatenar
print(nombre)
#print("Tienes: ",edad," años")
#int ->str
print("Tienes: "+str(edad)+" años")

#format string - fstring
#print("Los datos ingresados fueron: peso = {} kg y altura = {}m.".format(peso, altura))
print(f"Los datos ingresados fueron: peso = {peso} kg y altura = {altura} m.") #más usada
print(f"Tiene un IMC = {imc}. Gracias!")
print(f"Tiene un IMC = {imc:.2f}. Gracias!")
edad = input("Ingrese su edad: ")

while edad.isdigit() and int(edad) < 18:
    print("Edad inválida!")
    edad = input("Ingrese su edad: ") #si no cuenta con esta instruccion ciclo infinito


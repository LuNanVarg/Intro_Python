# while con condicion
# cliente = input("Ingrese nombre y apellido: ")
# while cliente == "" or len(cliente.split()) < 2 or not all (palabra.isalpha() for palabra in cliente.split()):
#     print("Error")
#     cliente = input("Ingrese nombre y apellido: ")
 
#forzar ciclo y corto con break
# while True: 
#     cliente = input("Ingrese nombre y apellido: ")
#     if cliente == "" or len(cliente.split()) < 2 or not all (palabra.isalpha() for palabra in cliente.split()):
#         print("Error")
#     else:
#         break

# #variable bandera    
datos_ok = True
while datos_ok:
    cliente = input("Ingrese nombre y apellido: ")
    if cliente == "" or len(cliente.split()) < 2 or not all (palabra.isalpha() for palabra in cliente.split()):
        print("Error")
    else:
        datos_ok = False
        
        



#siguientes instrucciones
    
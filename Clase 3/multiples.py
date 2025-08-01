# entrda < 4 gratis
# entre 4 y 18 años costo 500
# mayores a 18 costo 1000
# mayores de 65 costo 500



# Caso 1
# entrada
edad = 4

#proceso
if edad < 4:
    print("Ingreso gratis")
elif edad < 18:
    print("Su entrada vale : $500")
elif edad < 65:
    print("Su entrada vale : $1000")
else: #caso por efecto 
    print("Su entrada vale : $500")

# Caso 2
if edad < 4:
    print("Ingreso gratis")
elif edad < 18 or edad < 65: 
    print("")

############
# entrda < 4 gratis
# entre 4 y 18 años costo 500
# mayores a 18 costo 1000
# mayores de 65 costo 500

#caso 1
#entrada
edad = 4

#proceso
if edad < 4:
    precio = 0
elif edad < 18:
    precio = 600
elif edad < 65:
    precio = 1000
else: #caso por defecto
    precio = 500
    
#salida
print("Tu entrada cuesta $", precio)
    
    
# #caso 2
# if edad < 4:
#     print("Ingreso gratis")
# elif edad < 18 or edad > 65:
#     print("Su entrada vale : $500")
# else: #caso por defecto
#     print("Su entrada vale $1000")
    
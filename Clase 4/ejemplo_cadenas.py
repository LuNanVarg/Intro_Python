
# indice
# gmedina
# 0 = g
# 1 = m
# 2 = e

nombre_usuario = 'gmedina'
# slicing
inicial = nombre_usuario[0:1]
apellido = nombre_usuario[1:]
print(inicial, "-", apellido)
correo = "gmendez@gmail.com"
extension = correo[-4:]
print(extension)
print(nombre_usuario.find("med"))
print(nombre_usuario.find("mez"))
cuit = "20-30222666-8"
cuit_separados  = cuit.split("-") #lista
print(cuit_separados)
dni = cuit_separados[1]
print(dni)


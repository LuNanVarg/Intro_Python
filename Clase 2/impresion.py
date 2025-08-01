
#impresion.py
# atajos de VS code
# ctrl+n nuevo
# ctrl+s guardar
# ctrl+k +c comentar en bloque
# ctrl+k +u descomentar en bloque
# caracteres de escape
# \n salto de línea
# \t tabulador
# \\ escape


# nombre = "Ada"
# print(f"{nombre:>10}") #Alineado a la derecha
# print(f"{nombre:<10}") #Alineado a la izquierda
# print(f"{nombre:^10}") #Centrado

nombre = 'Ada'
apellido = 'Lovelace'
profesion = 'Programadora'
email = "alovelace@gmail.com"
telefono = 549458545

#Impresion en formato de tarjeta
print("="*40,"DATOS PERSONALES","="*40) #mostrar 40 veces el simbolo =
print(f"\tNombre: {nombre}")
print(f"\tApellido: \t{apellido}\n")
print(f"\tProfesion: \t{profesion}")
print(f"\tTeléfono: \t{telefono}")
print("-"*80) #mostrar 40 veces el simbolo =
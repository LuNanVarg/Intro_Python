#ejemplo-while2.py
password = input("ingrese su contraseña: ")
confirmacion = input("ingrese nuevamente: ")

while password != confirmacion:
    print("❌Las contraseñas no coinciden")
    password = input("ingrese su contraseña: ")
    confirmacion = input("ingrese nuevamente: ")

print("✔ Contraseña confirmada exitosamente!")
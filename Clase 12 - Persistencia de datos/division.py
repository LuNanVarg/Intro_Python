print("Ingresa dos valores y los divido")
print("Presione 's' para salir")

while True:
    primer_nro = input("Primer número: ")
    if primer_nro.lower() == 's':
        break
    segundo_nro = input("Segundo número: ")
    try:
        respuesta = float(primer_nro)/ float(segundo_nro)
    except ZeroDivisionError:
        print("No puede dividir por 0.")
    except ValueError:
        print("Ingrese valores numéricos")
    else:
        print(f"Resultado: {respuesta}")
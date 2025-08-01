#ciudades.py
#usando break para salir del loop


prompt = "\n Ingresa las ciudades que visitaste. "
prompt += "\n Ingresa 'salir' para finalizar. "
prompt += "\n"

while True:
    ciudad = input(prompt)
    
    if ciudad.lower() == "salir":
        break
    else:
        print("Visitaste: ", ciudad)

print("Siguen las instrucciones de mi programa")

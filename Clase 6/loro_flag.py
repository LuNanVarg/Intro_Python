#loro_flag.py
# prompt = "Ingrese su edad: "
# edad = input(prompt)

prompt = "\n Dime algo y lo repito"
prompt += "\n Ingresa 'salir' para finalizar. "
prompt += "\n"

activo = True #variable bandera

while activo:
    mensaje = input(prompt)
    if mensaje.lower() == "salir":
        activo = False
    else:
        print(mensaje)
    
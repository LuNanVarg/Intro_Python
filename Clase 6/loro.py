
prompt = "\n Dime algo y lo repito"
prompt += "\n Ingresa 'salir' para finalizar "
prompt += "\n"

#activo = True # Variable bandera
#mensaje = ""
while mensaje.lower() != "salir":
      mensaje = input(prompt)
      if mensaje.lower() != "salir":
            print(mensaje)

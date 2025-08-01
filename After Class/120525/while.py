while True:
    texto = input("Ingrese texto: ")
    if len(texto) > 5 and texto.isalnum():
        print("Texto válido: ", texto)
        break
    else:
        print("Texto inválido")
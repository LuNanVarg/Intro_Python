
#ejemplo de listas
#recorrer listas

bebidas = ['fernet', 'cerveza', 'vino', 'gancia']
print(bebidas)

#sale mal => revisar!
for bebida in bebidas:
    #print(bebida)
    if 'n' in bebida:
        print(bebida)
        bebidas.remove(bebida)
    #print(bebidas)
print(bebidas)

# pasando un nro arbitrario de argumentos
def hacer_pizza(*toppings):
    '''
    Imprime la lista de toppinggs del pedido
    '''
    print("Su pedido incluye: ")
    for topping in toppings:
            print(f"\t {toppings}")

# mezclar arbitrario
def hacer_pizza_size(porciones, *toppings):
    '''
    Imprime la lista de toppinggs del pedido con tamaño
    '''
    print(f"Su pedido de {porciones} porciones incluye ")
    for topping in toppings:
            print(f"\t {toppings}")


# main
hacer_pizza('pepperoni')
hacer_pizza('calabreza')
hacer_pizza(12, 'anchoas', 'tomate')
hacer_pizza(16, 'jamon','morrones', 'aceitunas')

# investigación mix: parametros posicionales, arbitrarios y por default ??? 
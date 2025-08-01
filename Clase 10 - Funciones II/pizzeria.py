#pasando un nro arbitrario de argumentos- usamos una tupla
def hacer_pizza(*toppings):
    '''
    Imprime la lista de toppings del pedido
    '''
    print("Su pedido incluye: ")
    for topping in toppings:
        print(f"\t {topping}")
# mezclar arbitrario con posicionales
def hacer_pizza_size(porciones, *toppings):
    '''
    Imprime la lista de toppings del pedido con tamaño 
    '''
    print(f"Su pedido de {porciones} porciones incluye: ")
    for topping in toppings:
        print(f"\t {topping}")
    
#main
#hacer_pizza('pepperoni')
#hacer_pizza('jamón', 'morrones', 'aceitunas')
#hacer_pizza_size(12, 'calabresa')
#hacer_pizza_size(16, 'anchoas','queso')

#investigacion mix: parametros posicionales, arbitrarios y por default ?????



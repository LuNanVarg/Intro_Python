#pizzeria.py
# lista almacenado como valor de una clave
pizza = {
    'tamaño': 8,
    'toppings': ['aceituna', 'morrones', 'jamon', 'extra queso']
}


print(f"Ud. ordenó una pizza de {pizza['tamaño']} porciones. Con los siguientes toppings: ")
for topping in pizza['toppings']:
    print(f"\t * {topping.title()}")
    
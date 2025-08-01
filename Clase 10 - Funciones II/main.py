# main.py

# 1.importamos todo el módulo
# import nombre_modulo (trae todos las funciones)
# import pizzeria #mportamos el módulo

# 2.importamos una funcion especifica
# from modulo import nombre_funcion
# from pizza import hacer_pizza

# 3.uso de alias a una funcion
# from modulo import nombre_funcion as alias
# from pizzeria import hacer_pizza as hp

# 4.uso de un alias a un módulo
# import pizzeria as pz
# matplotlib as mpl

# 5.importanndo todas las funciones del módulo (Es el más usado)
from pizzeria import * #all

# 1.invocar - cuando importo todo el módulo
# pizzeria.hacer_pizza(12, 'anchoas', 'tomate')
# pizzeria.hacer_pizza(16, 'jamon','morrones', 'aceitunas')

# 2.invocar - cuando importo una función específica
# hacer_pizza(12, 'anchoas', 'tomate')
# hacer_pizza(16, 'jamon','morrones', 'aceitunas')

# 3.invocar - cuando uso un alias para una función
# hp(12, 'anchoas', 'tomate')
# hp(16, 'jamon','morrones', 'aceitunas')


# 4.invocar - cuando importo todo el módulo usando un alias
# pz.hacer_pizza(12, 'anchoas', 'tomate')
# pz.hacer_pizza(16, 'jamon','morrones', 'aceitunas')


# 5.invocar utilizando el operador *
hacer_pizza(12, 'anchoas', 'tomate')
hacer_pizza(16, 'jamon','morrones', 'aceitunas')
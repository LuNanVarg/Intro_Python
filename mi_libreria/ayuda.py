#ayuda.py

from clientes import actualizar_cliente_id

#Visualizar docstrings o documentación de forma nativa
help(actualizar_cliente_id)

print(actualizar_cliente_id.__doc__)

#Visualizar a travez de una herramienta
# sphinx
# en la consola: pip install sphinx
# en la raiz del proyecto sphinx-quickstart
# responder las preguntas 
# en build-conf.py agregar 
#import os
#import sys
#sys.path.insert(0, os.path.abspath('../../'))


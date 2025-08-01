#alien3.py
alien = {'color': 'amarillo', 'posicion_x': 0, 'posicion_y': 25, 'velocidad': 'media'}
#lento incremento 1
#media incremento 2
#rapdio incremento 3
if alien['velocidad'] == 'lento':
    incremento_X = 1
elif alien['velocidad'] == 'media':
    incremento_X = 2
else:
    incremento_X = 3
    
alien['posicion_x'] = alien['posicion_x'] + incremento_X

print(f"La nueva ubicación del alien es {alien['posicion_x']}")
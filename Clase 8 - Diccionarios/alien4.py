#alien4.py
alien_0 = {'color':'verde', 'puntaje': 5}
print(alien_0)

#eliminar
del alien_0['puntaje']
print(alien_0)

#pop
alien = {'color': 'amarillo', 'posicion_x': 0, 'posicion_y': 25, 'velocidad': 'media'}
alien.pop('posicion_y')
print(alien)

#popitem
eliminado = alien.popitem()
print("eliminado: ", eliminado) #tupla
print(alien)

#updte
alien_0 = {'color':'verde', 'puntaje': 5}
alien_1 = {'color': 'amarillo', 'puntaje': 10, 'velocidad': 'lenta'}
alien_1.update(alien_0)
print(alien_1)
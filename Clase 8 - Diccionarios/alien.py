
alien_0 = {'color':'verde', 'puntaje': 5}
print(alien_0)

print(alien_0['color']) #verde
print(alien_0['puntaje']) #5
print(f"el alien {alien_0['color']} tiene asignado {alien_0['puntaje']} puntos.")

# agregar nuevo par de clave valor
alien_0['posicion_x'] = 0
alien_0['posicion_y'] = 25

print(alien_0)

alien_0['velocidad'] = 'media'
print(alien_0)



motos = ['zanella','honda', 'yamaha', 'fencor', 'motomel']
print(motos)

motos[0] = 'ducati'
print(motos)

#cliente =[nombre, apellido, direccion]
#cliente =["Carlos", "Perez" "Bolivar 333"]
#cliente[0] = 'Carla'

#agregar elementos a la lista
motos = ['honda','yamaha', 'bmw'] 
print(motos)
motos.append('kawasaki')
print(motos)


motos = [] #lista vacia 
print(motos)
motos.append('zanalla')
motos.append('honda')
motos.append('yamaha')
print(motos)

#insertar elementos a una lista 
motos = ['honda','yamaha', 'bmw'] 
print(motos)
motos.insert(0, 'ducati' )  
print(motos)

#eliminar elementos 
#del
motos = ['honda','yamaha', 'bmw'] 
print(motos)
del motos[1]
print(motos)

#pop() -> elimina el ultimo y lo retiene en ememoria
motos = ['honda','yamaha', 'bmw'] 
print(motos)
moto_eliminada = motos.pop() #bmw
print("Usted eliminó: " +moto_eliminada)

#pop(1) 
moto_eliminada = motos.pop(1) 
print("Usted eliminó: " + moto_eliminada)
print(motos)

#eliminar dado un valor 
motos = ['honda','yamaha', 'bmw'] 
print(motos)
if 'ducati' in motos: #asegurarse de que el valor esté en la lista
   motos.remove('ducati')
else: 
   print("Ducati no está en la lista")

motos.remove('bmw')
print(motos)


nombre = input('¿Como se llama?: ')
edad = input('¿Cuantos años tiene?: ')
direccion = input('¿Donde vive?: ')
telefono = input('¿Cual es su numero de telefono: ')
persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
print(persona['nombre'], 'tiene' , persona['edad'], 'años, vive en ', persona['direccion'], 'y su numero de telefono es ', persona['telefono'])
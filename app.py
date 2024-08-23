import random

print("Bienvenido a tu Generador de Contraeñas!")
print("Sigue las instrucciones para generar tu nueva contraseña!")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£¢∞§¶•ªº().,0123456789'

number = input('Cantidad de Contraseñas a Generar: ')
number = int(number)

lenght = input('Introduce la longitud de tu contraseña: ')
lenght = int(lenght)

print ('\nAqui estan tus contraseñas: ')

for pwd in range(number):
    passwords = ''
    for c in range(lenght):
        passwords += random.choice(chars)
    print(passwords)

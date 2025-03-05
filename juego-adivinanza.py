

import random


numero_secreto = random.randint(0,100)
cant_intentos = 0
cant_max= 5
adivinado = False

print ("Bienvenido a mi juego misterioso")

while not adivinado:
    if not cant_intentos < cant_max:
        break
    numero = int (input("Introduce un numero del 1 al 99: ")) #Si no pongo o casteo a INT dara error, ya que INPUT da STR.

    if numero == numero_secreto:
        print ("Felicitaciones, adivinaste el numero secreto")
        adivinado = True
    elif numero < numero_secreto:
        print ("El numero secreto es mayor al seleccionado")
    else:
        print ("El numero secreto es menor al seleccionado")
   
    cant_intentos += 1

if not cant_intentos < cant_max:
    print ("GAME OVER")
# Si quiero agregar cantidad de intentos tengo que agregar
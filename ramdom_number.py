import random
aleatorio = (random.randint(1, 50))

playing = True 
while playing: 
    guess = int (input ("Ingresa un numero "))
    if guess == aleatorio:
        print ("Ganaste TESO")
        playing = False 
    elif guess <= aleatorio:
        print ("Tu numero es menor")

    else:
        print ("Tu numero es mayor")
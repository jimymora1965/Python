import random

print("\tBienvenido al juego para adivinar números")

nombre = input("Ingresa tu nombre:\n")
print(f"hola {nombre}, Generare un nombre del 1 al 100. Tienes 8 oportunidades para que lo adivines!!!")

intentos = 1

x = random.randint (1, 100)

while intentos <= 8:
    numero = int(input("ingresa un numero entre 1 y 100:\n"))
    if numero <= 0 or numero >100:
        print("\tHaz ingresado un valor erroneo!!") 
        continue
    intentos = intentos + 1
    if numero < x:
        print("\tEl numero a adivinar es mas alto:")
    elif numero > x:
        print("\tEl número a adivinar es mas bajo:")
    
    elif  numero == x:
        print(f"{nombre} adivinastes.  Es el {numero}, lo lograste en el intento No. {intentos-1}\n")
if numero !=x:
    print(f"Has superado el numero de oportunidades, estas en el intento {intentos}\n")
   

   
    
    
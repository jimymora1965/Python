num = "Ingresa un numero y te dire si es par o impar\n"
num+= "(Escribe 'salir' para cerrar el programa)\n"
preguntar = True

while preguntar:
    numero = input(num)
    if numero == "cerrar":
        preguntar= False
    else:
        numero = int(numero)
        if numero % 2 == 0:
            print(f"\tEl numero {numero} es par\n")
        else:
            print(f"\tEl numero {numero} es impar\n")

print("Escribiste 'cerrar!!!. Has salido del programa\n")

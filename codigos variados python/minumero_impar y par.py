mensaje = "Escribe un numero para saber si es par o impar\n"
mensaje+= "(Escribe 'cerrar' para salir del programa)\n"
preguntar = True

while preguntar:
    numero = input(mensaje)
    if numero == "cerrar":
        preguntar = False
    else:
        numero = int(numero)
        if numero % 2 == 0:
            print(f"\tEl numero {numero} es par")
        else:
            print(f"\tEl numero {numero} es impar")

print("Escribiste 'cerrar' por lo tanto saliste del programa")



pregunta = 'Agrega un número y te dire si es par o impar:\r\n'
pregunta += '(Escribe "Cerrar" para salir de la aplicacion)\r\n'
preguntar = True

while preguntar:
    numero = input(pregunta)
    if numero == 'cerrar':
        preguntar = False
    else:
        numero = int(numero)
        if numero % 2 == 0:
            print("El numero es par")
        else:
            print("El numero es impar")

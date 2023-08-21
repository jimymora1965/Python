# Excepciones

while True:
    try:
        numero = int(input("Ingrese su edad: "))
        break
    except ValueError:
        print("ERROR, no es un número")

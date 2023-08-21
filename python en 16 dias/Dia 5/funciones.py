def saludo():
    print("Hola mundo")
saludo()

print("\n")
def nom(nombre):
    print(nombre)
nom("jimy")


def saludar():
    print('"¡Hola mundo!"')
saludar()


def nombre_persona(nombre):
    print('"Bienvenido" ' + nombre)
    
nombre_persona("Jimy")


#return
def suma(num1,num2):
    print(num1 + num2)
    return suma
suma(10,2000)


#otro return
def sum(num3,num4):
    return num3 + num4
resultado = sum(12,15)
print(resultado)

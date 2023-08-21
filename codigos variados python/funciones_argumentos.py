# Funciones y argumentos opcionales

def Funcion_Multiplicar(numero1, numero2, num3=5):
    return (numero1*numero2) - num3


rpta = Funcion_Multiplicar(3, 6)
print(rpta)


def ListaNombres(*nombres):
    for n in nombres:
        print(n)


ListaNombres("Maria", "Juan", "Luis", "Alberto")

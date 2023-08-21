#argumentos variables 2

def operacion(*args):
    total = 0
    
    for valor in args:
        total = total + valor
    return total
print("Suma:\n")
print(operacion(5+6+7))

print("Multiplicacion\n")
print(operacion(4*5*8))



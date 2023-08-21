def operacion(*args):
    total = 0
    for valor in args:
        total = total + valor
    return total
print("Suma:")
print(operacion(1+2+3))

print("Division:")
print(operacion(30//2))

print("Multiplicacion:")
print(operacion(1*2*3*4*5))


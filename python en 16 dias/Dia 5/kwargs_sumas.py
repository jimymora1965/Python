
print("Suma de args:")
print('==============')

def suma(*args):
    s = 0
    for arg in args:
        s += arg
    return s
total = suma(5,6,7,8,9)
print(total)

print("====================")

print("Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.")
def suma(**kwargs):
    s = 0
    for key, value in kwargs.items():
        print(key, "=", value)
        s += value
    return s
    
suma(a=3, b=10, c=3)
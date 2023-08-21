def cantidad_atributos(**kwargs):
    cantidad = 0
    for clave in kwargs.items():
        cantidad += 1
    return cantidad
print(cantidad_atributos('x: '10','y':'20')


def op(*args):
    total = 0
    for operacion in args:
        total = total + operacion

    return total
print(op(5,4))


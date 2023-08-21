def suma(**kwargs):
    s = 0
    for llave, valor in kwargs.items():
        print(f'{llave} = {valor}')
        s+=1
    return s
resultado = suma(valor1  =  10, valor2 = 20)
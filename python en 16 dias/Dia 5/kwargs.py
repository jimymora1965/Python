def prueba(num1, num2, *args, **kwargs):
    print(f'El primer valor es: {num1}')
    print(f'El segundo valor es: {num2}')
    
    for arg in args:
        print(f'arg = {arg}')
        
    for clave, valor in kwargs.items():
        print(f'Kwargs: {clave} = {valor}')
        
args= [100,200,300,400]
kwargs = {'x': 'uno','y':'dos','z':'tres'}
prueba(13,17,*args,**kwargs)



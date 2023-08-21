def prueba(num1, num2, *args,**kwargs ):
    print(f'El numero 1 es: {num1}')
    print(f'El numero 2 es: {num2}')
    
    for arg in args:
        print(f'Los arg son = {arg}')
        
    for clave, valor in kwargs.items():
        print(f'Los valores de kwargs son: {clave} = {valor}')
        
args = [1,2,3,4,5,6]    
kwargs = {'x':'uno', 'y': 'dos'}
prueba(1,2,*args,**kwargs)

print('----------------------------')
print('Segundo ejemplo con **kwargs')
print('----------------------------')



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




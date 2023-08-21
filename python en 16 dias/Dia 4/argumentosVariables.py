# para sumar todos los argumentos que posea una funcion
print("Para utilizar todos los elemnentos de una funcion")
def suma(*args): # lo importante es el asterisco
    total = 0
    
    for arg in args:
        total = total + arg
    return total
print(suma(4,5,6,7,8,12))

def op(*args):
    total = 0
    for operacion in args:
        total = total + operacion
        
    return total
print(op(5,4))
    

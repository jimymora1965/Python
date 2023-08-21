# fibonacci 01123581321
a = 0
b = 1
c = 0
contador = 1
while contador<20:
    print(b)
    c = a+b
    a = b
    b = c
    contador+= 1

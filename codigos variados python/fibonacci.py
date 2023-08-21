#SERIE FIBONACCI
#11235813...


a=0 #2 3
b=1 #3 5
c=0 #3 5
contador = 1
while contador <= 100:
    print(b)
    c=a+b
    a=b
    b=c
    contador = contador +1
    

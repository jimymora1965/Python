#Números Primos
#2, 3, 5, 7...
"""
for n in range(2, 10):
    es_primo=True
    for x in range(2, n):
        if n % x == 0:
           print(n,"NO ES PRIMO")
           es_primo=False
           break
        if es_primo:
            if x == n-1:
                print(n,"ES PRIMO")
            
    if n==2:
        print(n,"ES PRIMO")
"""

#Numeros Primos forma correcta

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
           print(n,"NO ES PRIMO")
           break
    else:
        print(n, "ES PRIMO")

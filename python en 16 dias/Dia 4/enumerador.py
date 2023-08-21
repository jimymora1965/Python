from random import randint

lista = ['a','b','c','d']
indice = 0
for item in lista:
    print(indice, item)
    indice = indice + 1
 
 #con enumerate   
lista = ['a','b','c','d']

for item in enumerate(lista):
    print(item)
  
#con rango  
print("\n")

for item in enumerate(range(50,55)):
    print(item)
         
print("\n")
   #random      
suerte = randint(1, 99)
print(suerte)
print("\n")

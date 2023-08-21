dic = {"jose": "el valiente", "mario": "el peligroso"}
for clave, valor in dic.items():
    print(clave, valor)

for x,y in enumerate([5,9,2,4,0,1]):
    print(x,y)

lista1 = ["banana","naranja"]
lista2 = ["melon","papaya"]
for l1,l2 in zip(lista1,lista2):
    print(l1,l2)

for x in reversed(range(1,7,2)):
    print(x)

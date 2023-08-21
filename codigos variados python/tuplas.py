tupla1 = (1,3,"t",False)
print(tupla1)#imprimo la tupla

tupla2 = ([1,2,3],4,5,6)
print(tupla2)#tupla con lista anidada

mitupla = tupla2[0]#para poder ver solo la lista dentro de la tupla
print(mitupla)

mitupla[0]= 999#para poder modificar la lista dentro de la tupla
print(mitupla)

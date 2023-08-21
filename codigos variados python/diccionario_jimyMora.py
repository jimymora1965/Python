# MI DICCIONARIO
carro = {}
print(carro)

carro['Modelo'] = 1900
carro['Marca'] = 'Mercedes Benz'
print(carro)
carro['Modelo'] = 2010
carro['Marca'] = 'Toyota'
print(carro)
carro['Modelo'] = 2020
carro['Marca'] = 'Renault'
print(carro)

#accediendo a la marca de un auto
x = carro['Marca']
print(x)

#accediendo con get
carro['Modelo'] = 1900
carro['Marca'] = 'Mercedes Benz'


x = carro.get('Modelo','Marca')
print(x)


print ("carro['Modelo']: ", carro['Marca'])


#accediendo a todos los valores de la lista
x = carro.values()
print(x)


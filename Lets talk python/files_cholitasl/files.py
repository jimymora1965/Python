from io import open

"""
 # con este codigo practico cosas del menu!!!!!!!
 
f = open('drinks.txt')
drinks = f.read()
print(drinks)

print('\tCon readlines el print muestra una lista:\n')
f = open('drinks.txt')
drinks = f.readlines()
print(drinks)

print()


print('Con este codigo eliminamos los "\\n" que aparecen al imprimir con readlines:\n')

f = open("drinks.txt")
temp = f.readlines()
drinks = []
for item in temp:
    new_item = item.strip()#el metodo strip() elimina los saltos de linea de readlines
    drinks.append(new_item)
print(drinks) """

# con este codigo utilizo una funcion para ver el menu sin repetir codigo

def read_menu(menu):
    f = open(menu)
    temp = f.readlines()
    result = []
    for item in temp:
        new_item = item.strip()
        result.append(new_item)
        
    return result
    
drinks = read_menu("drinks.txt")
print(drinks)
flavors = read_menu("flavors.txt")
print(flavors)
toppings = read_menu("toppings.txt")
print(toppings)
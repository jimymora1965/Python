def menu(choices, title="Cholitas, pan artesanal", prompt = "Elige tu menu:\n"):
    print(title)
    print(len(title)* "-")
    i = 1
    for c in choices:
        print(i, c)
        i += 1
    choice = input(prompt)
    answer = choices[int(choice)-1]
    
    return answer

#creo variables con sus atributos
panes = ['Pistacho', 'Bocadillo', 'Vainilla', 'Finas Hierbas', 'Quesos']
postres = ['3 Leches', 'Maracuya', 'Napoleón']
bebidas = ['Limonada De Coco', 'Corozo', 'Yerbabuena', 'Apio']

# llamo la funcion

pan = menu(panes, 'Cholitas Panes', 'Selecciona un delicioso pan:\n ')
print(f'Has seleccionado:\n {pan}')
print()
postre = menu(postres, 'Cholitas Postres', 'Selecciona un delicioso postre:\n')
print(f'Tu postre elegido:\n  {postre}')
print()
bebida = menu(bebidas, 'Cholitas Bebidas', 'Selecciona una refrescante bebida:\n')
print(f'Tu bebida seleccionada es:\n {bebida}\n')

print('\tAquí está tu orden\n')
print('Producto principal: ', pan)
print('Postre: ', postre)
print('Bebida: ', bebida)


    


def menu(choices, title, prompt):
  print(title)
  print("----------------------")
  i = 1
  for c in choices:
    print(i, c)
    i +=1
  choice = input(prompt)
  answer = choices[int(choice)]
  return answer

drinks =['Chocolate', 'Café', 'Decaf']
flavors = ['Caramelo', 'Vainilla', 'Durazno']
toppings = ['Chocolate', 'Canela', 'Caramelo']
choice = menu( drinks, 'Erick drinks', 'Elija su bebida:\n')
print(choice)
  
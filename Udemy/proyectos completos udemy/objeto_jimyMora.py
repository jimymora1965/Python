jugador={}
print(jugador)

jugador['nombre']= "Christian"
jugador['Edad'] = 24
print(jugador)

jugador['Edad'] = 50
print(jugador)

jugador['nombre:'] = "Carlos"
jugador['Edad:'] = 45
print(jugador)

for llave, valor in jugador.items():
    print(llave)
    print(valor)
    
b = jugador['Edad:']
print(b)

#accediendo a todos los valores de la lista
x = jugador.values()
print(x)

print(jugador)


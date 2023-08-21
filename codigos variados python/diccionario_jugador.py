# diccionario_jugador
jugador = {
}
print(jugador)

#añadamos puntajes
jugador['nombre:'] = 'Jimy'
jugador['puntaje:'] = 0
print(jugador)
jugador['puntaje:'] = 100
print(jugador)
jugador['puntaje:'] = 200
print(jugador)
print()
#accediendo a un valor
print(jugador.get('consola',"No existe ese valor"))
print(jugador.get(200))
print(jugador)
print()
#iterando
print("Iterando sobre el objeto")
for llave,valor in jugador.items():
    #print(llave,valor)
    print(llave)
    print(valor)

#eliminenos un valor
del jugador['puntaje:']
print(jugador)






cancion = {
   'artista' : 'Metallica',
   'cancion' : "It doesn't matter",
   'lanzamiento' : '1995',
   'likes' : 3000
   }
print(cancion)
print(cancion['artista'])
print()
#mezclando con un string
print(f"Estoy escuchando: {cancion['cancion']}")
print()
#añadiendo nuevos valores
cancion['playlist'] = 'Heavy metal'
print(cancion)
print()
#reemplazando un elemento
cancion['cancion'] = 'Los guaduales'
print(cancion)
print()
#eliminando un elemento
del cancion['likes']
print(cancion)










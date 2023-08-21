playlist = {}
playlist['canciones'] = []

def app():
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('Nombre playlist')
        if nombre_playlist:
          playlist['nombre'] = nombre_playlist
          agregar_playlist = False
          
          agregar_canciones()
          
def agregar_canciones():
  agregar_cancion = True
  while agregar_cancion:
    mensaje = f"\nAgrega canciones para la play list {playlist['nombre']}\n"
    mensaje+= ('Escribe "X" ó "x" para ver la lista de canciones')
    cancion = input(mensaje)
    if mensaje == "X" or mensaje == "x":
      agregar_cancion = False
    else:
      playlist['nombre'].append(cancion)
    

app()
#ddddddddddddddddddddddddddddddddddddddddddddddddddd


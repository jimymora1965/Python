playlist = {}
playlist['canciones'] = []

def app():
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('Nombre Playlist:\n')
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False

            agregar_canciones()

def agregar_canciones():
      # bandera para agregar canciones
    agregar_cancion = True

    while agregar_cancion:

        #nombreCancion = playlist['nombre']

        #solicitar al usuario canciones para agregar a la playlist creada
        pregunta = f"\nAgrega canciones para la play list {playlist['nombre']}\n"
        pregunta += 'Escribe "X" ó "x" para dejar de agregar canciones\n'

        cancion = input(pregunta)
        if cancion == 'X' or cancion == 'x':
            # Dejar de agregar canciones
            agregar_cancion = False

            # Mostrar resumen de la playlist
            mostrar_resumen()
        else:
            # agregar las canciones a la playlist
            playlist['canciones'].append(cancion)

def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print("")
    print(f'Playlist: {nombre_playlist}\n')
    print('\tCanciones:\n')
    for cancion in playlist['canciones']:
        print(cancion)


app()
#comentario sin utilidad para practicar solamente
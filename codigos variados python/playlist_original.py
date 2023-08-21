playlist = {}  # diccionario vacio que va almacenando las playlist que creo
playlist['canciones'] = []  # lista vac a de canciones que creo

# funcion principal que llama a las demas funciones para que el programa funcione


def app():
    # agregar playlist
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('Como desea nombrar la playlist:\n')
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist

            # ya tenemos un nombre, desactivar el true
            agregar_playlist = False

            # Mandar a llamar la funcion para agregar canciones
            agregar_canciones()


def agregar_canciones():
    # bandera para agregar canciones
    agregar_cancion = True

    while agregar_cancion:
        # preguntar al usuario que canción desea agregar
        nombre_playlist = playlist['nombre']
        pregunta = f"\nAgrega canciones para la play list {nombre_playlist}\n"
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
    print(f'Playlist: {nombre_playlist}\n')
    print('Canciones:\n')
    for cancion in playlist['canciones']:
        print(cancion)


app()

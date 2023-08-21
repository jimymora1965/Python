playlist = {}
playlist['canciones'] = []

def app():
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('Nombre playlist:\n')
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False
            agregar_cancion()

def agregar_cancion():
   agregar_cancion = True
   while agregar_cancion:
       mensaje = (f"Agregar cancion a la lista {playlist['nombre']}\n")
       mensaje+= ('Escriba "X" o "x" para cerrar la app\n')
       cancion = input(mensaje)
       if cancion == "X" or cancion == "x":
           agregar_cancion = False
           mostrar_resumen()
       else:
            playlist['canciones'].append(cancion)

def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print("")
    print(f'Playlist: {nombre_playlist}')
    print('\tCanciones:\n')
    for cancion in playlist['canciones']:
        print(cancion)

app()

playlist = {}
playlist['nombre'] = []

def app():
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('Nombre playlist')
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False


            print(playlist)



app()

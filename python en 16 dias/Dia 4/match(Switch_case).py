cliente = {'Nombre': 'jimy',
           'edad': 57,
           'ocupacion': 'programador'}

pelicula = {'titulo': 'Matrix',
            'ficha_tecnica': {'protagonista': 'keanuv reeves',
                              'director': 'hermanos washowsky'}}

elemento = [cliente, pelicula]
print(elemento)

for e in elemento:
    match e:
        case  {'Nombre': nombre,
           'edad': edad,
           'ocupacion': ocupacion}:
                print("Es un cliente")
                print(nombre, edad, ocupacion)
       
        case {'titulo': titulo,
            'ficha_tecnica': {'protagonista': protagonista,
                              'director': director}}:
                print("es una pelicula")
                print(f"\ttitulo: {titulo},\n protagonista: {protagonista},\n director: {director}")
        case _:
                print('N se que es esto')        
                
        
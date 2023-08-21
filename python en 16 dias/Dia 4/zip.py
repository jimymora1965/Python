nombre = ['Jimy','Erica','Valentina']
edades = [57,43,23]
ciudad = ['San Andres', 'Valledupar', 'Bogota']

combinados = list(zip(nombre, edades,ciudad))

for nombre, edades, ciudad in combinados:
    print(f"{nombre} tiene {edades} y es de {ciudad}")

#lee el archivo completo
archivo = open("texto_de_dalto.txt",encoding="UTF-8")

""" #lee el archivo completo
archivo = archivo.read()
print(archivo) """

#ojo: para volver a leer el archivo debe cerrarlo porque una vez abierto no me deja leerlo otra vez

""" #para leer linea por linea por linea
lineas = archivo.readlines()
print(lineas) """

""" #para leer una sola linea
lineas = archivo.readline()
print(lineas) """

#Siempre hay que cerrar el archivo
archivo.close()
print(archivo.read())

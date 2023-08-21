with open("texto_de_dalto.txt", encoding = "UTF-8") as archivo:
    print(archivo.read())
    
    contenido = archivo.read()
    print(contenido)
#cuando se usa with open no es necesario cerrar el archivo con close()
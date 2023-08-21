#Lectura y escritura de archivos

#r = read
#w = write
#a = append
#r+ = read and write

archivo = open("texto.txt", "a", encoding='utf-8')
#texto = archivo.read(6)
#texto = archivo.readline()
archivo.write("Hola")
archivo.close()

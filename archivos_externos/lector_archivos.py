from io import open

direccion_archivo = 'archivos_externos2/digitos_pi.txt'
with open(direccion_archivo) as archivo:
    contenido = archivo.read()
    print(contenido)
    
print()

print("\tPara imprimir las lineas en forma separada:\n")
direccion_archivo = 'archivos_externos2/digitos_pi.txt'
with open(direccion_archivo) as archivo:
    for linea in archivo:
        print(linea)
        
print()

print("Usando el metodo 'rstrip' para quitar los espacios entre las lineas")
direccion_archivo = 'archivos_externos2/digitos_pi.txt'
with open(direccion_archivo) as archivo:
    for linea in archivo:
        print(linea.rstrip())
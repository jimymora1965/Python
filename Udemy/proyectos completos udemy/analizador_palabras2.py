texto = input("INGRESE UN TEXTO A ELECCIÓN\n")
letras = []

texto = texto.lower()

print("Contando letras:\n")
letras.append(input("Ingrese la primera letra del texto: " .lower()))
letras.append(input("Ingrese la segunda letra del texto: " .lower()))
letras.append(input("Ingrese la tercera letra del texto: " .lower()))

print("\n")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} en el texto")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2}  en el texto")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} en el texto")

print("\n")

print("Contando las palabras del texto:\n")
palabras = texto.split()
print(f"Encontramos {len(palabras)} palabras en el texto")

print("\n")
print("Letra inicial y letra final:\n")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial es {letra_inicio} y la final es {letra_final}")

print("\n")
print("Texto invertido\n")
palabras.reverse()
texto_invertido = " " .join(palabras)#el join hace que se eliminen las comillas al hacer print
print(texto_invertido)

print("\n")
print("Buscando la palabra python")
buscar_python = 'python' in texto
dic = {True: 'Si', False: 'No'}
print(f"La palabra ´Python' {dic[buscar_python]} esta en el texto")


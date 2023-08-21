import re

texto = '''Hola maestro esta es la cadena 1, como estas mi capitan?
Esta es la linea 2 de texto
y Esta es la fina (linea 3) definitivamete mi capitan__'''

print("Expresiones regulares")

""" #Haciendo una busqueda simple
#resultado = re.findall("Esta", texto, flags = re.IGNORECASE)#este flag ignora el CASE
resultado = re.findall("Esta", texto)#solo busca las que empiezan con mayuscula pq asi la escribi
print(resultado)
  """
  
""" # \d busca los digitos del 0 al 9, con la d en minuscula
resultado = re.findall(r"\d",texto)
print(resultado) """

""" #\D busca todo menos valores numericos
resultado = re.findall(f"\D",texto)
print(resultado) """

""" #\w busca todos los caracteres alfanumericos incluyendo guion bajo
resultado = re.findall(r"\w",texto)
print(resultado) """

""" #\ busca todos los caracteres menos los alfanumericos, los espacios se ven como ''
resultado = re.findall(r"\W",texto)
print(resultado) """

""" #\s busca todos espacios en blanco, tabs, saltos en linea
resultado = re.findall(r"\s",texto)
print(resultado) """

""" #\S busca todo menos los espacios en blanco, tabs, saltos en linea
resultado = re.findall(r"\S",texto)
print(resultado)"""
 
"""#El punto "." busca todo menos  saltos en linea
resultado = re.findall(r".",texto)
print(resultado)"""


"""#El punto "." busca todo menos  saltos en linea
resultado = re.findall(r".",texto)
print(resultado) """

""" #para buscar saltos de  linea
resultado = re.findall(r"\n",texto)
print(resultado)"""


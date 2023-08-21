    #metodo join
lista_palabras = ["La","legibilidad","cuenta."]

a = "La"
b = "legibilidad"
c = "cuenta."
d = " ".join([a,b,c])
print(d)

#metodo replace
texto = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado = texto.replace("difícil", "fácil")
print(resultado)

resultado2 = resultado.replace("mala", "buena")
print(resultado2)
print("")


#hacer salto de linea con comillas triples
poema = """Mil pequeños peces blancos
como si hirviera 
el color del agua"""
print(poema)

#concatenar 15 veces la palabra "repexticion"
print("repeticion + " * 15)

poema = """Tierra mojada
mis recuerdos de viaje,
entre las lluvias"""

print("agua" is not poema)


frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
frutas.pop(3)
print(frutas)


#2 listas, una con nombre y la otra con apellido
nombres = ["jimy", "valentina", "erica", "christian"]
apellidos = ["mora","martinez","diaz","aaron"]

#registrar esta informacion en un txt en forma optima

with open("archivos_problemas_resueltos\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n------------\n")for n,a in zip(nombres,apellidos)]

""" #este codigo es lo mismo que el anterior pero en otro orden. Genera un txt
for n, a in zip(nombres,apellidos):
    arch.writelines(f"Nombre: {n}\nApellidos: {a}\n---------\n") """


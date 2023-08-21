#clases

"""class Restaurante:
    x = "arroz"
    y = "papa"
p1 = Restaurante
print(p1.x)
print(p1.y)"""

"""class Person:
   def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("jimy",50)

print(p1.name)
print(p1.age)"""

"""
#llamando una funcion
class Person:
    def __init__(self,name,age):
      self.name = name
      self.age = age

    def myFunction(self):
        print("Hello, my name is:" + self.name)

p1 = Person("Jimy",57)
p1.myFunction()"""


"""
#cambiando el self por otro valor que yo desee.
class Person:
    def __init__(yomismo,name,age):
      yomismo.name = name
      yomismo.age = age

    def myFunction(yomismo):
        print("Hello, my name is:" + yomismo.name)

p1 = Person("Jimy",57)
p1.myFunction()"""


"""
#contatenando
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def myfunction(self):
        print("Hola mi edad es: ", self.edad, " y mi nombre es: " + self.nombre)
p1 = Persona("Valentina", 23)
p1.myfunction()"""

#modificar un atributo
"""class Person:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def myfunction(self):
        print("Hola mi nombre es: " + self.nombre)

p1 = Person("Valentina", 43)
p1.edad = 40
print(p1.edad)"""

"""
# metodo delete eliminando un atributo.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunction(self):
        print("My name is: "+ self.name)

p1 = Person("Jimy", 57)
del p1.age
print(p1.age)"""

"""
#eliminando un objeto
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunction(self):
        print("my name is: " + self.name)

p1 = Person("jimy", 57)
del p1
print(p1)"""






































































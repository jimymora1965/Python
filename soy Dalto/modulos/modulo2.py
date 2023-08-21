#con este import busco la carpeta funciones_buenas, el modulo saludar yu la funcion saludar
""" import funciones_buenas.saludar

print(funciones_buenas.saludar.saludar("mocca"))

 """
import sys
#print(sys.builtin_module_names) los devuelve todos los modulos que estan el python

sys.path.append("c:\\Users\\jimym\\Documents\\Python_mis_cursos\\soy Dalto\\importando_modulos2")

#print(sys.path)#muestra la ruta de los modulos

#ya conociendo la ruta de los modulos imprimo lo que tengo en mi modulo

import saludar2

print(saludar2.saludar2("Jaime"))
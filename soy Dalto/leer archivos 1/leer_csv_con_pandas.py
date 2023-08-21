import pandas as pd
df = pd.read_csv("datos.csv")
df2 = pd.read_csv("datos.csv")  # utilizo este para concatenar

""" #con esta linea con names le ponemos encabezado a la lista del block
df = pd.read_csv("datos.csv", names = ["name","lastname","age"]) """


""" #muestra todos los elementos de la lista en block de notas
print(df)
 """

""" #OBTENIENDO LOS DATOS DE LA COLUMNA NOMBRE
print(df["nombre"]) """

""" #ordenando el dataframe por edad de mayor a menor
df_ordenado = df.sort_values("edad", ascending= False)
print(df_ordenado)
 """
""" #ordenando el dataframe por edad de menor a mayor
df_ordenado = df.sort_values("edad")
print(df_ordenado) """

""" #para concatenar dos df(df=dataframe)
df_concatenado = pd.concat(([df,df2]))
print(df_concatenado) """

""" # accediendo a las primeras filas con head
primer_fila = df.head(3)
print(primer_fila) """

""" "accediendo a las ultimas 3 filas con tail"
ultimas_filas = df.tail(3)
print(ultimas_filas)
 """
 
 #accediendo a la cantidad de columnas y filas con shape
 
filas_y_columnas_totales = df.shape
print(filas_y_columnas_totales)

""" #para saber el numero de filas, recordando que es un indice que empieza en 0.
filas_totales = filas_y_columnas_totales[0]#0 porque es el indice de fila
print(filas_totales)

columnas_totales = filas_y_columnas_totales[1]#1 porque es el indice de columna
print(columnas_totales) """

""" #otra forma es desempaquetando
filas_totales, columnas_totales = df.shape
print(filas_totales)
print(columnas_totales) """



""" #accediendo a un elemento especifico del df con loc
elemento_especifico_loc = df.loc[2,"edad"]
print(elemento_especifico_loc)
 """
 
"""  #accediendo a un elemeno especifico pero con iloc (la i de iloc = indice)
elemento_especifico = df.iloc[2,2]#el primer 2 = es el indice de la columna edad
                                   #el segundo 2 es el indice de la fila a buscar
print(elemento_especifico)#dará 44. columna 2, fila 2 buscando desde el indice 0. """


""" #accediendo a todas las filas de una columna con loc
apellidos = df.loc[:,"apellido"]#muestra todos los apellidos de la columna 1(apellidos).
print(apellidos) """


""" #accediendo a todas las filas de una columna con iloc
apellidos = df.iloc[:,2]#muestra todos los apellidos de la columna 1(apellidos).
print(apellidos) """

""" #accediendo a la fila 3 con loc. // como es fila se usa indice
fila_3 = df.loc[2,:]
print(fila_3)
 """
""" #accediendo a la fila 3 con iloc. Recordar que la i de iloc = indice//como es fila se usa indice
fila_3 = df.iloc[2,:]
print(fila_3) """

""" #accediendo a filas cuya edad sea mayor a 30
mayor_30 = df.loc[df["edad"]>30,:]
print(mayor_30) """

#accediendo a filas cuya edad sea menor a 40
menor_40= df.loc[df["edad"]<40,:]
print(menor_40)



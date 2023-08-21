#cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("datos.csv")

 #convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)


""" #mostrar el tipo de dato del primer elemento de la columna edad
print(type(df['edad'][0]))#el [0] es el 0 de la datos.csv """

 #imprime el indice 3 de datos.csv
print(df['edad'][3])#el [3] es el 3 de datos.csv


#reemplazaremos en la columna apellido
df['apellido'].replace('perea','barrios', inplace=True)
print(df['apellido'])

#si hay filas con datos incompletos para llenarlas con NaNa
df = df.dropna()
print(df)

#eliminando filas repetidas

df = df.drop_duplicates()
print(df)

#creando un CSV con el dataframe resultante(limpio)
df.to_csv("datos_limpios.csv")
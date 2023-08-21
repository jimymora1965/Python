#"a"= append, para agregar texto
with open("texto_de_dalto.txt","a", encoding= "UTF-8") as archivo:
   """ #puedo hacerlo asi o con un for 
   archivo.write("\tAgregando texto al block de notas")
    """
   for i in range(5):
       archivo.write(f"Linea{i+1} agregada\n")
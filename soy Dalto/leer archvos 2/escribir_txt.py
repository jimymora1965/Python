with open("texto_de_dalto.txt","w", encoding= "UTF-8") as archivo:
    """ #sobreescribiendo el archivo
    archivo.write(("Estoy añadiendo texto al archivo")) """
    
    "agrego lineas al archivo txt. para ver el resultado corro el codigo sin print"
    archivo.writelines(["hola maestro\n", "saludos\n"])
    archivo.writelines(["no te he visto en la isla\n", "en San Andres.\n"])
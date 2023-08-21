def app():
    archivo = open('archivo.txt','w')#w = es para escritura, sino existe lo creará
    
    #generar numros en archivos
    for i in range(0, 20):
        archivo.write('Esta es la linea ' + str(i) + "\r\n")
       
    archivo.close()
    
app()

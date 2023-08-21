def Dividir(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Error no se puede dividir entre 0")
    else:
        print("La respuesta es ",result)
    finally:
        print("Se termino el programa")

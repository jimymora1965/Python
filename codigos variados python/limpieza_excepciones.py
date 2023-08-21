#Metodos de Limpieza en excepciones


def Dividir(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        raise ZeroDivisionError("No se puede dividir entre 0")
    else:
        print("La respuesta es ", result)
    finally:
        print("Se terminó el programa")

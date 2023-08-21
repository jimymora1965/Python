def suma():
    while True:
        a = input("Numero 1:")
        b = input("Numero 2:")
        try:
            resultado = int(a) + int(b)
        except ValueError as e:
            print("Debes ingresar un numero")#esta linea se ejecuta si hay una excepcion
            print(f"Error: {e}")
        else:
             break #esta linea se ejecuta si no hay una excepcion
        finally:
            print("Manejo de excepciones finalizado")
            
    return resultado

    
print(suma())

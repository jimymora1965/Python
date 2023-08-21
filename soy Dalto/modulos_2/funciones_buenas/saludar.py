#en este ejemplo la carpeta esta por fuera de modulos. vamos a importar su modulo
#utilizaremos el ejemplo con modulo3
#con este codigo imprimimos __name__ en el modulo 3 cuando llame al modulo saludar
def saludar(name):
    return f"Hola {name} como estas?"

print(__name__)
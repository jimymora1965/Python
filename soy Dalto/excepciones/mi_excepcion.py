class MiExcepcion(Exception):
    def __init__(self, err):
        print("Cometiste el siguiente error: {e}")

try:
    raise MiExcepcion("Persona poco culta")

except:
    print("No cometas ese tipo de error")
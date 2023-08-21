#Anidacion de sentencia if
"""
calificacion = 5

if calificacion >= 15:
    print("APROBADO")
else:
    if calificacion >=12:
        print("APROBADO PERO FALTA ESTUDIAR MAS")
    elif calificacion >=8:
        print("DESAPROBADO, PERO VA A SUPLETORIOS")
    else:
        print("DESAPROBADO")
"""
"""
#Anidacion de sentencia for

for a in range(1,10):
    for b in range(1,10):
        print("O", end="")
    print("")
"""   
        
# Triangulo con while
conteo=1
while conteo <= 10:
    conteoUnido=1
    while conteoUnido <= conteo:
        print("*", end="")
        conteoUnido=conteoUnido+1
    print("")
    conteo=conteo+1
        

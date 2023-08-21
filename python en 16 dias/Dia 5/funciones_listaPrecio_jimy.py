precio_cafe = ('Moka', 2.0),('Expresso', 3.45),('Capuchino', 6.7)

def cafe_mas_caro(precio_cafe):
    precio_mayor = 0
    nombre_cafe = ''
    
    for cafe, precio in precio_cafe:
        if precio > precio_mayor:
            precio_mayor = precio
            nombre_cafe = cafe 
            
        else:
            pass
    return(nombre_cafe,precio_mayor)
cafe, precio = cafe_mas_caro(precio_cafe)
print(f"El cafe mas costoso es el {cafe}, cuyo precio es {precio}")
        
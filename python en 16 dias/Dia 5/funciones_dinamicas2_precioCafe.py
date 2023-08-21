lista_precios = ('Capuchino', 1.5),('Expreso', 2.5),('Moka', 10.9)#esta es una tupla
               #[('Capuchino', 1.5),('Expreso', 2.5),('Moka', 10.9)] esta tambien es una tupla pero con corchetes

def cafe_mas_costoso(lista_precio):
    precio_mayor = 0
    nombre_cafe = ''#para que me imprima el nombre del cafe mas caro
    
    for cafe, precio in lista_precio:
        if precio > precio_mayor:
            precio_mayor = precio
            nombre_cafe = cafe
            
        else:
            pass
    return(nombre_cafe, precio_mayor)
cafe,precio = cafe_mas_costoso(lista_precios)
print(f"El café más caro es {cafe}, cuyo precio es {precio}")
                 
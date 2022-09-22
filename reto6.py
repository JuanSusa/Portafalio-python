"""
Estamos de aniversario y vamos a regalarte un descuento por compras superiores a los $50.000
Pon a jugar tu suerte..... 
Si sacas una bola roja obtendras un descuento del 10% al valor de tu compra.
Si sacas una bola azul, obtendras un descuento del 30% al valor de tu compra.
Si sacas una bola amarilla, obtendras un descuento del 50% al valor de tu compra.
Si sacas una bola blanca, tu compra sera totalmente gratis.
"""


from random import randint

eleccion=int(input("inserte 1 para registrar factura \n inserte 2 para registrar cantidad de productos \n"))
if eleccion==1:
    factura=int(input("ingrese el valor de la factura \n"))
else:
    cantidaProductos=int(input("ingrese la cantidad de productos \n"))
    valorProducto=10000
    factura=cantidaProductos*valorProducto

print("Bienvenidos a Supermecados Noe")
bola=randint(1,4)
totalCompra=int(input("Ingrese el valor de la compra\n"))

if totalCompra>=50000 and bola==1:
    total=totalCompra-((totalCompra*10)/100)
    print("!Felicidades, Ganaste un descuento del 10%")
    print("El valor en total a pagar es de",total)
    
elif totalCompra>=50000 and bola==2:
    total=totalCompra-((totalCompra*30)/100)
    print("!Felicidades, Ganaste un descuento del 30%")
    print("El valor en total a pagar es de",total)

elif totalCompra>=50000 and bola==3:
    total=totalCompra-((totalCompra*50)/100)
    print("!Felicidades, Ganaste un descuento del 50%")
    print("El valor en total a pagar es de",total)

elif totalCompra>=50000 and bola==4:
    total=totalCompra-((totalCompra*100)/100)
    print("!Felicidades, Tu compras es totalmente !Gratis¡")
    print("El valor en total a pagar es de",total)        
else:
    print("Lo sentimos, sigue intentando")
if bola==1 or bola==2 or bola==3:
    valorCancelar=int(input("ingrese en valor con el cual va a cancelar \n"))
    vueltas=valorCancelar-total
    print=(f"el total de la compra es de {total}\n productos registrados me \n cancela con {valorCancelar}\n su cambio es de {vueltas}")
else:
    bola==4
    print("!Felicidades, Tu compras es totalmente !Gratis¡")

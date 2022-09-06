numProductos=int(input("ingrese el numero de productos a comprar"))
valorProducto=10000
factura=numProductos*valorProducto
print("la cantidad de productos comprados son de: ", numProductos, "el valor total a pagar es de: ", factura)

valorCancelar=int(input("ingrese el valor com el que va a cancelar"))
cambio=valorCancelar-factura
print("la cantidad de productos son ", numProductos, "usted cancela con", valorCancelar, "su cambio es de", cambio)


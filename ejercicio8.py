presupuesto=100000
gastoc=0

while  presupuesto>=0 and presupuesto<=100000:
    gasto=int(input("ingrese el valor de su gasto \n"))

    if presupuesto>=0 and presupuesto<=100000:
    
        presupuesto=presupuesto-gasto
        gastoc=gastoc+1
        print(f"el gasto fue, {gasto} y su saldo es de {presupuesto}")

        if gastoc <=2:
            print("la compra continua")
       
        else:        
            break
    else:
        print("Fondos insuficientes")
print("")
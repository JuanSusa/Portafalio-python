from random import randint


saldo=0
repeat="s"
repetir="S"
azar=0


while repeat=="s" or repeat=="S":
    cash=int(input("Ingrese el valor a recagar\n"))
    saldo=saldo+cash
    print(input(f"Su saldo actual es de {saldo}"))
    if saldo>=0:
        repeat=(input("Si desea hacer otra recarga escriba si, o de lo contrario escriba no \n"))
    else:
        break
apuesta=int(input("¿Cúanto desea apostar?\n"))
while repetir=="s" or repetir=="S":
    moneda=randint(1,2)
    eleccion=int(input("digite 1 para Cara y 2 para Sello \n"))

    if moneda==1 and eleccion==1:
        saldo=saldo+apuesta
        azar=azar+1
        print("felicidades, !ganaste¡ \n" "escogiste Cara y salio Cara")
    elif moneda==1 and eleccion==2:
        saldo=saldo+apuesta
        azar=azar+1
        print("Lo siento, sigue intentando !Perdiste¡ \n" "escogiste Sello y salio Cara")
    elif moneda==2 and eleccion==2:
        saldo=saldo-apuesta
        azar=azar+1
        print("felicidades, !ganaste¡ \n" "escogiste Sello y salio Sello")
    elif moneda==2 and eleccion==1:
        saldo=saldo-apuesta
        azar=azar+1
        print("Lo siento, sigue intentando !Perdiste¡ \n" "escogiste Sello y salio Cara")
    elif eleccion!=1 and eleccion!=2:
        print("Escogiste un numero incorrecto")
    else:
        print("datos incorrectos")
    print("Saldo actual",saldo)
    repetir=input("¿Quiere seguir jugando? Ingrese S para si o N para No\n")
    if repeat=="s" or repeat=="S":
        apuesta=int(input("¿Cúanto desea apostar?"))

print(f"Las rondas del juego fueron {azar} y el dinero que gano en total fue de {saldo}" )

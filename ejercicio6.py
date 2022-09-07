from random import randint


moneda=randint(1,2)
eleccion=int(input("digite 1 para Cara y 2 para Sello \n"))

if moneda==1 and eleccion==1:
    print("felicidades, !ganaste¡ \n" "escogiste Cara y salio Cara")
elif moneda==1 and eleccion==2:
    print("Lo siento, sigue intentando !Perdiste¡ \n" "escogiste Sello y salio Cara")
elif moneda==2 and eleccion==2:
    print("felicidades, !ganaste¡ \n" "escogiste Sello y salio Sello")
elif moneda==2 and eleccion==1:
    print("Lo siento, sigue intentando !Perdiste¡ \n" "escogiste Sello y salio Cara")
elif eleccion!=1 and eleccion!=2:
    print("Escogiste un numero incorrecto")
else:
    print("datos incorrectos")
    
print(f"la moneda cayó {moneda}")

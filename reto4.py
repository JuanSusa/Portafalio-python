from random import randint

print("Vamos a jugar Piedar, Papel o Tijera \n" "donde vas marcar del 1 al 3 según con lo quieras jugar \n" "En donde 1, es Piedra \n" "2 es Papel y \n" "3 es Tijera \n" )

juego=randint(1,3)
eleccion=int(input("Digite un numero para empezar a jugar \n"))

if juego==1 and eleccion==2:
    print("!Felicidades¡, Ganaste \n" "Salio Piedra")
elif juego==2 and eleccion==3:
    print("!Felicidades¡, Ganaste \n" "Salio Papel")
elif juego==3 and eleccion==1:
    print("!Felicidades¡, Ganaste \n" "Salio Tijera")
else:
    print("Hay un Empate")
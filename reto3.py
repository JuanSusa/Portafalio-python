from random import randint


craps=randint(1,6)
craps2=randint(1,6)

print("lanza los dados y ganas si \n" "sale un par de 1 en los dos dados \n" "sale un total de 3 en los dos dados \n" "sale un total de once en los dos dados \n" "se obtiene dos o doce en los dos dados \n" "sale un total de siete en los dos dados \n")
print(f"Lanza los dados {craps,craps2}")

if craps==1 and craps2==1:
    print("!Felicidades, Ganaste¡ \n" "Salio un par de 1")
elif craps==1 and craps2==2 or craps==2 and craps2==1:
    print("!Felicidades, Ganaste¡ \n" "Salio un total de 3")
elif craps==5 and craps2==6 or craps==6 and craps2==5:
    print("!Felicidades, Ganaste¡ \n" "Salio un total de 11")
elif craps==1 and craps2==1 or craps==6 and craps2==6:
    print("!Felicidades, Ganaste¡ \n" "Salio un total de 2 o 12")
elif craps==3 and craps2==4 or craps==4 and craps2==3 or craps==2 and craps2==5 or craps==5 and craps2==2:
    print("!Felicidades, Ganaste¡ \n" "Salio un total de 7")
else:
    print("Lo siento, perdiste \n" "resultado inconrrecto")
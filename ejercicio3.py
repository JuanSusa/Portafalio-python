edad=int(input("ingresa la edad en años \n"))

if 0<=edad<=4:
    print("el cliente ingresa gratis") 
if 4<=edad<=18:
    print("el cliente debe pagar 20.000")
if 18<=edad<=60:
    print("el cliente debe pagar 15.000")
if edad>60:
    print("el cliente solo pagara el valor de 3.000")

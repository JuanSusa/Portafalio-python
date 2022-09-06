pesoBebe=int(input("cual es el peso del bebe "))
edadBebe=int(input("cual es la edad del bebe "))

##calculamos la dosis a aplicar##
peso=pesoBebe+10
edad=edadBebe*10

dosisVacuna=pesoBebe/edadBebe*8

print("La dosis a aplicar es ", dosisVacuna)
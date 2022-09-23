#definir una lista
#siempre se especifican dentro de un corchete
lista=[] #Esta lista esta vacia
lista2=[1,2,3,4]
print(lista2)

#Acceder a una posicion especifica atraves del index o posicion
print(lista2[2])
#Ultimo elemnto de la lista
print(lista2[-1])
#Penultimo elemento de una lista
print(lista2[-2])
#Modificar un elemnto de una posicion especifica
lista2[0]=7
print(lista2)
#Recorrer la lista 2 y multiplicar por 2 los elementos
for l in lista2:
    print(l*2)
#incluir el index en el recorrido, la iteracion de la lista
for index,l in enumerate(lista2):
    print(f"la posiucion{index} se encuentra el valor {l}")



numeros=[5,9,10]
generos=["jazz","Rock","Djent"]
#recorrer dos listas en un ciclo
for n,g in zip(numeros,generos):
    print(f"El numero {n} esta asociado con el genero {g}")


#Ordenar Listas

#Orden Ascendente


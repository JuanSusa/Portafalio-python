onces=["Hamburguesa","Sandwich","Pizza"]
print(onces)
#Agregar un solo elmento en una posicion especifica 
onces.insert(2,"Empanadas")
print(onces)
#Agregar un solo elemento al final de una lista
#onces.append("Bebida")
#print(onces)

#Agregar varios elemnetos al final de una lista
onces.extend(["Malteada","Perro Caliente"])
print(onces)



#Borrar un elemento de una lista
#onces.remove("Empanadas")

#Borrar un elemento de una posicion especifica
#del onces[0]

#Borrar el ultimo elemento de una lista
#onces.pop()

#Eliminar la lista en su totalidad
#onces.clear()

#Devuleve la posicion de un elemento
print(onces.index("Empanada"))
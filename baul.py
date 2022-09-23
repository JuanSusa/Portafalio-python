baul=[]
seguir="s"
while seguir=="s" or seguir =="S":
    print("Seleccione 1. Agregar un elemento a la lista \n 2. Listaer articulos del baul \n 3.Borrar ultimo elemento del baul\n 4. Borrar articulo especifico del baul")
    de=int(input("Que opcion deseas realizar"))
    if de==1:
        baul.append(input("ingrese el nombre del articulo a agregar"))
    elif de==2:
        print(input("Estos son los articulos de tu baul"))
        baul.sort()
        print(baul)
    elif de==3:
        print(input(f"Vas a eliminar el articulo {baul[-1]}"))
        baul.pop()
        print(baul)
    elif de==4:
        for index,b in enumerate(baul):
            print(input(f"# {index} => {b}"))
            baul.remove(int(input("Ingrese el numero del articulo que desea eliminar")))
            print("El baul quedo asi",baul)
    else:
        print("opcion incorrecta")          

    seguir=input("Desea regresar al menu S/s N para terminar")
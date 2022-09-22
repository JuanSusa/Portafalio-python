definitiva=0
total=0
for i in range(0,4,1):
    nota=float(input("ingrese el valor de la nota \n"))
    print(f"la suma total de la nota es, {nota}")
    total=total+nota
definitiva=total/4
print(f"la nota definita es {definitiva}")
if definitiva<=0 and nota<=2.9:
    print("reprobo la asignatura")
elif definitiva <=4.0:
    print("Pasa raspando la asignatura")
elif definitiva >=4.1:
    print("aprobo la asignatura")
else:
    print("valores errados")
# Programa que pide el dia de la semana del 1 al 7 y escriba el dia correspondiente
# Si se intruce otro numero da error

print("Programa que pide el dia de la semana del 1 al 7 y escriba el dia correspondiente")
print("Si se intruce otro numero da error")
print("\n")

numero = int(input("Introduce un numero del 1 al 7: "))

if numero == 1:
    print("Lunes")
elif numero == 2:
    print("Martes")
elif numero == 3:
    print("Miercoles")
elif numero == 4:
    print("Jueves")
elif numero == 5:
    print("Viernes")
elif numero == 6:
    print("Sabado")
elif numero == 7:
    print("Domingo")
else:
    print("Error")


#Programa que pide 3 numero enteros y diga cual es mayor. Sin funcion max

print("Programa que pide 3 numero enteros y diga cual es mayor.")
print("\n")

num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
num3 = int(input("Introduce el tercer numero: "))

if num1 > num2 and num1 > num3:
    print("El numero mayor es: ", num1)
elif num2 > num1 and num2 > num3:
    print("El numero mayor es: ", num2)
else:
    print("El numero mayor es: ", num3)

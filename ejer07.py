#Programa que pide 5 numeros enteros y diga cual es mayor. No se puede utiliza funcion max()

print("Programa que pide 5 numeros enteros y diga cual es mayor.")
print("\n")

num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
num3 = int(input("Introduce el tercer numero: "))
num4 = int(input("Introduce el cuarto numero: "))
num5 = int(input("Introduce el quinto numero: "))

if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
    print("El numero mayor es: ", num1)
elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
    print("El numero mayor es: ", num2)
elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
    print("El numero mayor es: ", num3)
elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
    print("El numero mayor es: ", num4)
else:
    print("El numero mayor es: ", num5)

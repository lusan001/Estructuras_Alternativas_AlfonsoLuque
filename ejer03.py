print("Este programa te dice si un año es bisiesto o no" "\n")
print("Para que un año sea bisiesto debe cumplir con las siguientes condiciones:" "\n")
print("1. Que sea divisible entre 4")
print("2. Que no sea divisible entre 100")
print("3. Que sea divisible entre 400")
print("....")
print("\n")

anyo = int(input("Ingresa un año: "))

if anyo // 4 == 0 and anyo // 100 != 0 or anyo // 400 == 0 :
    print("Este es una año bisiesto")
else:
    print("Este no es un año bisiesto")
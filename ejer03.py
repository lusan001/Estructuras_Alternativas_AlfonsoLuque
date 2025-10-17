"""
Programa para determinar si un año es bisiesto.

Un año es bisiesto si cumple las siguientes condiciones:
1. Es divisible por 4
2. No es divisible por 100, a menos que también sea divisible por 400
"""

print("Este programa te dice si un año es bisiesto o no\n")
print("Para que un año sea bisiesto debe cumplir con las siguientes condiciones:\n")
print("1. Que sea divisible entre 4")
print("2. Que no sea divisible entre 100, a menos que también sea divisible por 400")
print("\n")

# Solicitar al usuario que ingrese un año
anyo = int(input("Ingresa un año: "))

# Verificar si es un año bisiesto
if (anyo % 4 == 0 and anyo % 100 != 0) or (anyo % 400 == 0):
    print(f"\nEl año {anyo} es bisiesto")
else:
    print(f"\nEl año {anyo} no es bisiesto")
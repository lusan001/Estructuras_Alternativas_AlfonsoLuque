"""
Programa para determinar el tipo de triángulo según las longitudes de sus lados.

El programa recibe tres valores numéricos (A, B, C) que representan las longitudes
de los lados de un triángulo y determina su tipo según las siguientes reglas:
1. Si cumple el teorema de Pitágoras: triángulo rectángulo
2. Si tiene dos lados iguales: triángulo isósceles
3. Si los tres lados son iguales: triángulo equilátero
4. Si no cumple ninguna de las condiciones anteriores, es escaleno.
"""

# Solicitar al usuario que ingrese las longitudes de los tres lados del triángulo
LadoA = float(input("Ingrese la longitud del primer lado: "))
LadoB = float(input("Ingrese la longitud del segundo lado: "))
LadoC = float(input("Ingrese la longitud del tercer lado: "))

#Si cumple el teorema de Pitágoras
if LadoA**2 + LadoB**2 == LadoC**2:
    print("El triángulo es rectángulo")

#Si tiene dos lados iguales
if LadoA == LadoB or LadoA == LadoC or LadoB == LadoC:
    print("El triángulo es isósceles")

#Si los tres lados son iguales
if LadoA == LadoB == LadoC:
    print("El triángulo es equilátero")

#Si no cumple ninguna de las condiciones anteriores
else:
    print("El triángulo es escaleno")
#Programa para convertir notas numericas en calificacion

nota = float(input("Introduce la nota: "))

if nota < 5:
    print("Suspenso")
elif nota < 7:
    print("Aprobado")
elif nota < 9:
    print("Notable")
elif nota < 10:
    print("Sobresaliente")
elif nota == 10:
    print("Matricula de honor")
else:
    print("Nota no valida")
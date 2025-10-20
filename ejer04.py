#Calcular el desglose minimo en billetes y monedas de una cantidad exacta de €
#Hay billetes de 500,200,100,50,20,10 y 5 € y monedas de 1 y 2€

cantidad = int(input("Introduce la cantidad de euros: "))

monedas_billetes = [500,200,100,50,20,10,5,2,1]

#
for billete in monedas_billetes:
    if cantidad >= billete:
        num = cantidad // billete
        cantidad = cantidad % billete
        print(num, "billetes de", billete)
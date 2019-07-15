n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())

lista = [n1, n2, n3, n4, n5, n6]

i = 0
positivos = []
while (i < len(lista)):
    if (lista[i] > 0):
        positivos.append(lista[i])
    i = i + 1

i = 0
resultado = 0
while (i < len(positivos)):
    resultado = resultado + positivos[i]
    i = i + 1

media = resultado / len(positivos)
qtde = len(positivos)

print("%d valores positivos" % qtde)
print("%.1f" % media)

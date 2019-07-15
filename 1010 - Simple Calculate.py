line1 = input().split(" ")
line2 = input().split(" ")

cod1 , quantity1, price1 = line1
cod2, quantity2 , price2 = line2


total = (int(quantity1) * float(price1)) + (int(quantity2) * float(price2))

print("VALOR A PAGAR: R$ %.2f" %total)

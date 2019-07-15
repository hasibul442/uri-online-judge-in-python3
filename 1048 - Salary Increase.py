a = float(input())

if a>=0 and a<=400:
    selary = a*(15/100.00)
    selary1 = a+selary
    per = 15
    print("Novo salario: %.2f"%selary1)
    print("Reajuste ganho: %.2f"%selary)
    print("Em percentual:",per,"%")

elif a>=400.01 and a<=800.00:
    selary = a*(12/100)
    selary1 = a+selary
    per = 12
    print("Novo salario: %.2f"%selary1)
    print("Reajuste ganho: %.2f"%selary)
    print("Em percentual:",per,"%")

elif a>=800.01 and a<=1200.00:
    selary = a*(10/100)
    selary1 = a+selary
    per = 10
    print("Novo salario: %.2f"%selary1)
    print("Reajuste ganho: %.2f"%selary)
    print("Em percentual:",per,"%")

elif a>=1200.01 and a<=2000.00:
    selary = a*(7/100)
    selary1 = a+selary
    per = 7
    print("Novo salario: %.2f"%selary1)
    print("Reajuste ganho: %.2f"%selary)
    print("Em percentual:",per,"%")

elif a>2000.00:
    per = 4
    selary = a * (per / 100)
    selary1 = a + selary
    print("Novo salario: %.2f" % selary1)
    print("Reajuste ganho: %.2f" % selary)
    print("Em percentual:", per,"%")

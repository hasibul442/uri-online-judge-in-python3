X,Y = input().split(" ")
X = int(X)
Y = int(Y)

if X==1:
    total = float(4.00*Y)
    print("Total: R$ %.2f"%total)
elif X==2:
    total = float(4.50 * Y)
    print("Total: R$ %.2f" % total)
elif X==3:
    total = float(5.00 * Y)
    print("Total: R$ %.2f" % total)
elif X==4:
    total = float(2.00 * Y)
    print("Total: R$ %.2f" % total)
elif X==5:
    total = float(1.50 * Y)
    print("Total: R$ %.2f" % total)

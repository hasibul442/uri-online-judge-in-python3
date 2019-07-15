import math
A,B,C = input().split(" ")
A = float(A)
B = float(B)
C = float(C)
if(A!=0):
    root = (B**2) - (4*A*C)
    if(root>0):
        R1 = (-B + math.sqrt(root)) / (2 * A)
        R2 = (-B - math.sqrt(root)) / (2 * A)
        print("R1 = %.5f" % R1)
        print("R2 = %.5f" % R2)
    elif (root < 0):
        print("Impossivel calcular")
else:
        print("Impossivel calcular")

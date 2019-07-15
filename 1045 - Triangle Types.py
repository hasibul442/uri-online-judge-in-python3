value = input().split()
value = list(map(float,value))

A,B,C = sorted(value) [::-1]

conti = True

if(A >= B+C):
    print("NAO FORMA TRIANGULO")
    conti = False

if(A**2 == (B**2) + (C**2) and conti):
    print("TRIANGULO RETANGULO")

if(A**2 > (B**2) + (C**2) and conti):
    print("TRIANGULO OBTUSANGULO")

if(A**2 < (B**2) + (C**2) and conti):
    print("TRIANGULO ACUTANGULO")

if(A == B and B == C and conti):
    print("TRIANGULO EQUILATERO")

if((A == B or B == C) and not (A == B and B == C) and conti):
    print("TRIANGULO ISOSCELES")

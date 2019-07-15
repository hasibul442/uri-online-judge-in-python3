N = float(input())

if N>0.00 and N<=2000.00:
    print("Isento")
elif N>=2000.01 and N<=3000.00:
    x= N-2000
    tex = x*0.08
    print("R$ %.2f" %tex)
elif N>=3000.01 and N<=4500.00:
    x= N-3000
    tex =( x*0.18)+(1000*0.08)
    print("R$ %.2f" %tex)
else:
    x= N-4500
    tex =(x*0.28)+(1500*0.18)+(1000*0.08)
    print("R$ %.2f" %tex)

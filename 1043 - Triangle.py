a,b,c = input().split(" ")
a=float(a)
b=float(b)
c=float(c)

if(a+b>c and b+c>a and a+c>b):
    print("Perimetro = %.1f"%(a+b+c))
else:
    print("Area = %.1f"%(0.5*(a+b)*c))

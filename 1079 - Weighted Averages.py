N = int(input())

for i in range(N):
    x1,x2,x3 = map(float,input().split(" "))
    x = (x1*2+x2*3+x3*5)/(2+3+5)
    print("%.1f" %x)

N = int(input())

for i in range(N):
    X,Y = map(int, input().split(" "))
    if Y==0:
        print("divisao impossivel")
    else:
        y =(X/Y)
        print("%.1f"%y)

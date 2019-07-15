N=int(input())

if N>5 and N<2000:
    for i in range(1,(N+1)):
        if(i%2==0):
            print("%d^2 = %d"%(i,i**2))

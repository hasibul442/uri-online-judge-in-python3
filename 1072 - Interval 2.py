A = int(input())

b=0
c=0

for i in range(A):
    B=int(input())
    if B>=10 and B<=20:
        b=b+1
    else:
        c=c+1
print("%d in"%b)
print("%d out"%c)

W = input().split()
W1 = int(W[1])
X1,X2,X3 = map(int,input().split(" : "))
Y = input().split()
Y1 = int(Y[1])
Z1,Z2,Z3 = map(int,input().split(" : "))

day = Y1-W1

hour = Z1-X1
if(hour<0):
    hour += 24
    day -= 1

minu = Z2-X2
if(minu<0):
    minu += 60
    hour -= 1

second = Z3-X3
if(second<0):
    second += 60
    minu -= 1

if(day<=0):
    day=0

print("%d dia(s)" %day)
print("%d hora(s)" %hour)
print("%d minuto(s)" %minu)
print("%d segundo(s)" %second)

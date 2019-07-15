input1 = input().split(" ")

A ,B ,C ,D = input1

sum1 = int(C)+int(D)
sum2 = int(A)+int(B)

if int(B)>int(C) and int(D)>int(A) and sum1>sum2 and int(C)>=0 and int(D)>=0 and int(A)%2==0:
     print("Valores aceitos")
else:
    print("Valores nao aceitos")

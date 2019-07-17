N = int(input())
total=total1=total2=total3=0
for i in range(N):
    a = input().split(" ")
    amount, name = a
    amount = int(amount)

    if(1<=amount<=15):
            total = total + amount
            if(name=='C'):
                total1=total1+amount
            if(name=='R'):
                total2=total2+amount
            if(name=='S'):
                total3=total3+amount

per1 = (total1/total)*100
per2 = (total2/total)*100
per3 = (total3/total)*100

print("Total: %d cobaias"%total)
print("Total de coelhos:",total1)
print("Total de ratos:",total2)
print("Total de sapos:",total3)

print("Percentual de coelhos: {:.2f} %".format(per1))
print("Percentual de ratos: {:.2f} %".format(per2))
print("Percentual de sapos: {:.2f} %".format(per3))

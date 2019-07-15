list1 = []
count=count1=count3=count2= 0

for i in range(0,5):
    x = int(input())
    list1.append(x)

for i in range(0,5):
    if(list1[i]%2==0):
        count = count+1
    else:
        count1 = count1 +1
for i in range(0,5):
    if(list1[i]>0):
        count2 = count2+1
    elif list1[i]<0:
        count3 = count3 +1

print(count,"valor(es) par(es)")
print(count1,"valor(es) impar(es)")
print(count2,"valor(es) positivo(s)")
print(count3,"valor(es) negativo(s)")

list1 = []
count= 0

for i in range(0,5):
    x = int(input())
    list1.append(x)

for i in range(0,5):
    if(list1[i]%2==0):
        count = count+1

print(count,"valores pares")

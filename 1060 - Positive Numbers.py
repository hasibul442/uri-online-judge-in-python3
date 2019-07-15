list1 = []
a = 6
coun = 0
for i in range (0,a):
    lis = input()
    list1.append(float(lis))
for i in range(0,a):
    if list1[i] >=0:
        coun =coun+1
print(coun,"valores positivos")

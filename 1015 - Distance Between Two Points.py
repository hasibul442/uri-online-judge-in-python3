import math
input1 = input().split(" ")
input2 = input().split(" ")

x1,y1 = input1
x2,y2 =  input2
distace = math.sqrt(((float(x2)-float(x1))**2)+((float(y2)-float(y1))**2))
print("%.4f"%distace)

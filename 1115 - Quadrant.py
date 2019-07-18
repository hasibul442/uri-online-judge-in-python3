X,Y = map(int, input().split(" "))

while (X != 0 and Y!=0):
    if(X>0 and Y>0):
        print("primeiro")
        X,Y = map(int, input().split(" "))
    elif(X<0 and Y>0):
        print("segundo")
        X,Y = map(int, input().split(" "))
    elif(X<0 and Y<0):
        print("terceiro")
        X,Y = map(int, input().split(" "))
    elif(X>0 and Y<0):
        print("quarto")
        X,Y = map(int, input().split(" "))
    else:
        print("")

input1 = input().split(" ")

A,B,C = input1
pi = 3.14159

rectangled_triangle = (1/2)*float(A)*float(C)
radius_circle = float(pi)*float(C)**2
trapezium = (1/2)*(float(A)+float(B))*float(C)
squar = float(B)**2
rectangla = float(A)*float(B)

print("TRIANGULO: %.3f"%rectangled_triangle)
print("CIRCULO: %.3f"%radius_circle)
print("TRAPEZIO: %.3f"%trapezium)
print("QUADRADO: %.3f"%squar)
print("RETANGULO: %.3f"%rectangla)

# Write a program to find the euclidean distance between two coordinates
import math

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

x=[x1,y1]
y=[x2,y2]

print("="*150)

print("Euclidean distance between given coordinates", round(math.dist(x,y),2))
import math
import random as rd

print(math.pi)
print(math.sin(38))
print(rd.randint(0, 10))

r = 100
print("Расчет 1 -", 2 * r * math.pi)
print("Расчет 2 -", (r ** 2) * math.pi)
print("Расчет 3 -", math.pow(r, 2) * math.pi)
x1 = 10
y1 = 10
x2 = 50
y2 = 100
l = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print("Расчет 4 -", l)
print("Факториал 1119 =", math.factorial(1119))

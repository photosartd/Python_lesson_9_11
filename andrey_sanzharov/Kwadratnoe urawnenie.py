a = float(input())
b = float(input())
c = float(input())
import math
D = float(b**2 - 4 * a * c)
if D > 0:
    x1 = float((-b + math.sqrt(D)) / (2 * a))
    x2 = float((-b - math.sqrt(D)) / (2 * a))
    print(x1, x2)
else:
    print('Не рассматривается по условию задачи')

import math
def equation(x, y, z):
    a = y**2 - 4*x*z
    if a < 0:
        print("Нет реальных решений.")
    elif a == 0:
        print("Есть только один корень.")
    else:
        d1 = (-y + math.sqrt(a))/(2*x)
        d2 = (-y - math.sqrt(a))/(2*x)
    return d1, d2

print(equation(1, 5, 6))

#x^2 + 5x + 6
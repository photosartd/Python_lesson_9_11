"""все что после 10 и двух ** - это степень десятки,
смотрите в чем она: в мегагерцах или килогерцах и меняйте цифорку
либо на 6 либо на 3 там где частота"""

import math

p = 1.7 * (10 ** (-8))  # удельное сопротивление
f = 1 * (10 ** 5)  # частота
m = 1.26 * (10 ** (-6))  # магнитная проницаемость
d = 2 * (10 ** (-3))  # толщина экрана


delt = math.sqrt(p / (math.pi * f * m))

E = 36 + 20 * math.log10(delt / p) + 8.7 * (d / delt)

print(E)

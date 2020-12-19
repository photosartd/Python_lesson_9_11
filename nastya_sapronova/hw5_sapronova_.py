m = int(input("Введите натуральное число: "))
i = 0
i_2 = 1
i_1 = 1
while i < m - 2:
    i_3 = i_1 + i_2
    i_1 = i_2
    i_2 = i_3
    i = i + 1
print(i_2)    








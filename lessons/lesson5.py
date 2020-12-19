#Циклы
#sum = 16
#for i in range(4):
#    sum = sum / 2
#    print(sum)

#Счётчик
#i = 1
#product = 1
#while i < 7:
#    i = i + 1
#    product = product * i
#    print(product)

#Запрашивает ввод числа с клавиатуры
# Находит максимальную цифру в это числе    
def max_in_number():
    #Введём переменную, которая будет наибольщей цифрой
    max = 0
    #Просим пользователя ввести число
    num = int(input("Введите число: "))
    while num > 0:
        rest = num % 10
        if max < rest:
            max = rest
            if (max == 9):
                break
        num = num//10
        print(num)
    return max

max = max_in_number()
print(max)
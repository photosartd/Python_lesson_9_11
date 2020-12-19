def count_odd_and_even():
    number = int(input("""Введите число, для которого мы посчитаем количество чётных и нечетных цифр: """))
    #Четные
    even = 0
    #Нечетные
    odd = 0
    while number > 0:
        rest = number % 10
        if rest % 2 == 0:
            even += 1
        else:
            odd +=1
        number = number // 10
    return even, odd

#Эта операция - распаковка, то есть в even и odd
#сейчас запишутся числа, которые возвращает функция
even, odd = count_odd_and_even()
print(f"Количество чётных цифр в числе: {even}, нечётных: {odd}")

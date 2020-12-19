#if - если
#else - иначе
#else if = elif - если иначе
#если "событие1" то "последовательность1"
#иначе "последовательность 2"
#and - и
#or - или
#not - не
andrey_is_a_student = False
andrey_age = 19

print(not andrey_age > 18)


if not andrey_age > 18:
    print('Andrey has not finished a school')
else:
    print("Andrey finished a school and not a student")


#a = int(input('Введите первое число: '))
#b = int(input('Введите второе число: '))
#if (a < b) or (b < a):
#    print("a - чётное")
#else:
#    print('a - нечетное')

#a != b - неравенство
#a == b - равеноство
#a >= b, a <= b
#a > b, a < b
# a = 2, b = 3
# (2 != 3) == (2 < 3) or (3 < 2)

#your_class = int(input("Введите ваш класс: "))
#if your_class == 9:
#    print('Вы в 9 классе')
#    your_letter = input("Введите букву вашего класса: ")
#    if your_letter == 'e':
#       print("Вы в классе под буквой 'e'")
#    else:
#        print("Вы в классе НЕ под буквой 'e'")
#elif your_class == 10:
#    print('Вы в 10 классе')
#elif your_class == 11:
#    print('Вы в 11 классе')
#else:
#   print("Вы не в 9, 10 или 11 классе")


total_count = 100
try:
    raw = input("Введите число: ")
    number = int(raw)
    total_count = total_count/number
except ValueError:
    print("Некорректное значение")
except ZeroDivisionError:
    print("Нельзя делить на 0")
except Exception:
    print("У вас ошибка неизвестного мне типа")
else:
    print("Else выполнился")
finally:
    print(total_count)

#Else - выполнится только в том случае, если в блоке try НЕ БЫЛО ошибок
#finally - выполнится ВСЕГДА после прохождения блока try - except



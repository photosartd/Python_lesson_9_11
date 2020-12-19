
misha_is_a_student = False
misha_age = 16 

print(misha_age < 16)

if misha_age < 18:
    print("Misha has not finished a school") 
else:     
   print("Misha hasn't finished a school and not a student")

   



your_class = int(input("Введите ваш класс: "))
if your_class == 9:
    print("Вы в 9 классе")
    your_letter = input("Введите букву вашего класса: ")
    if your_letter == "A":
        print("Вы в классе под буквой 'A'")
    else:
        print("Вы в классе НЕ под буквой 'A'")
elif your_class == 10:
    print("Вы в 10 классе")
    your_type = input("Введите профиль вашего класса: ")
    if your_type == "Физ-мат":
        print("Вы в классе с профилем Физ-мат")
    if your_type == "Хим-био":
        print("Вы в классе с профилем Хим-био")
    if your_type == "Соц-эконом":
        print("Вы в классе с профилем Соц-эконом")
elif your_class == 11:
    print("Вы в 11 классе")
else:
    print("Вы не в 9, 10 или 11 классе")





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




#У меня программа выдаёт "invalid syntax", в онлайн компиляторе всё работает
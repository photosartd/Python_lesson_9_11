
try:
    raw = input("Введите число от 0 до 59: ")
    number = int(raw)
    if (0 <= number <= 59):
        print("Всё верно")
except ValueError:
    try:
        raw = input("Попробуйте ещё раз: ")
        number = int(raw)
        if (0 <= number <= 59):
            print("Всё верно")
    except ValueError:
          print("Завершение работы программы")
    raw = input("Введите число от 0 до 59: ")
    number = int(raw)
if (0 <= number <= 59) :
    if (0 <= number <= 15) :
        print("I четверть")
    if (16 <= number <= 30) :
        print("II четверть")
    if (31 <= number <= 45) :
        print("III четверть")
    if (46 <= number <= 59) :
        print("IV четверть")
else:
    print("Число не лежит в интервале 0-59")
print()
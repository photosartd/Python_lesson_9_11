total_count = "Undefined value"
try:
    total_count = int(input("Введите число от 0 до 59: "))
except ValueError:
    try:
        total_count = int(input("Введите число еще раз: "))
    except ValueError:
        print("False type")
else:
    print("Выполняется тогда, когда не было exception")
finally:
    if (type(total_count) == str):
        pass
    else:
        if total_count>=0 and total_count<=15:
            print ("Число лежит в 1 четверти часа.")
        elif total_count>15 and total_count<=30:
            print("Число лежит во 2 четверти часа.")
        elif total_count>30 and total_count<=45:
            print("Число лежит в 3 четверти часа.")
        elif total_count>30 and total_count<=45: 
            print("Число лежит в 4 четверти часа.")
        else:
            print("Not in the interval")
try:
    total_count = int(input("Введите число от 0 до 59: "))
except ValueError:
    total_count = int(input("Введите число еще раз: "))
    if total_count > 59 and total_count < 0:
        print ("Число не лежит в заданном интервале.")
else:
    pass
finally:
    if total_count>=0 and total_count<=15:
        print ("Число лежит в 1 четверти часа.")
    elif total_count>15 and total_count<=30:
        print("Число лежит во 2 четверти часа.")
    elif total_count>30 and total_count<=45:
        print("Число лежит в 3 четверти часа.")
    else:
        print("Число лежит в 4 четверти часа.")



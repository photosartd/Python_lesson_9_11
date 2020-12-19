def count_iterations_and_result():
    while True:
        try:
            number = int(input("Введите число не меньше 500: "))
        except ValueError:
            print("Вы ввели не число!")
        else:
            if number < 500:
                print("Вы ввели число меньще 500")
                continue
            else:
                break
    counter = 0
    while number > 40:
        number /= 2
        counter += 1
    return number, counter


print(count_iterations_and_result())
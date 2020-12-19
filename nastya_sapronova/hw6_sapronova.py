def count():
    i = 0
    while True:
        try:
            a = int(input("Введите число равное или превышающее 500: "))
        except ValueError:
            continue
        if a < 500:
            continue
        else:
            break

    while a >= 40:
        a = a/2
        i = i + 1
    return a, i

print(count())

    








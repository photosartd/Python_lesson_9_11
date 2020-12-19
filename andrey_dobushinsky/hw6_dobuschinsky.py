def func():
    while 1==1 :
        try:
            a=float(input("введите число большее 500 ===> "))
            if a<500:
                print("число введено некоректо")
            else:
                break
        except ValueError:
            print("число введено некоректо")
    counter = 0
    while a > 40 :
        a /= 2
        counter += 1
    
    return a, counter

print(func())
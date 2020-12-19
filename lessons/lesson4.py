import math
#def = define - опредять, задавать
#smth = something - что-то
def gipotenuza(a, b):
    #Квадраты катетов
    a_sqr = a**2
    b_sqr = b**2
    #Сумма квадратов катетов
    sum_sqr = a_sqr + b_sqr
    #Гипотенуза
    c = math.sqrt(sum_sqr)
    return c

#print("Гипотенуза треугольника с катетами 8 и 6: ")
#katet_1 = 8
#katet_2 = 6
#print(gipotenuza(katet_1,katet_2))

#print("Гипотенуза треугольника с катетами 50 и 60: ")
#katet_11 = 50
#katet_22 = 60
#print(gipotenuza(katet_11,katet_22))

x = 10
name = "Misha"
def print_x():
    print(x)

def power(base=2, step=2):
    result = base**step
    return result

#print_x()
#print(x)

var = power()
print(var)

#sum_del_prod
#a, b
#возвращает сумму a и b деленную на их произведение

#def sum_del_prod(a, b):
#    return (a+b)/(a*b)

#print(sum_del_prod(4,5))


#Анонимная функция
my_func = lambda x, y: x + y
print(my_func(10, 20)) 

summa = my_func(1000, 4000)
print(summa)

#Вернётся true, если x > y, и false в другом случае
print((lambda x, y: x > y)(16, 15))

#sravnenie
#Принимает 3 аргумента x, y, z
#Возвращает True, если x < y и y < z и false в другом случае
sravnenie = lambda x, y, z: x < y and y < z
print(sravnenie(3,2,3))

print(type(my_func))

name = "Dima"
surname = "Trofimov"

product = lambda x, y: x > y

print(product(x=name, y=surname))

#Создание функции с неизвестным числом аргументов
def my_f(*args):
    for word in args:
        print(word)

my_f(name, surname)
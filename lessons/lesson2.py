#name = input("Введите ваше Имя: ")
#age = input("Введите ваш возраст: ")
#print(type(name), name, type(age), age)

color = "Green"
print(type(color))

my_age = 21
print(type(my_age), my_age)

height = 182.5
print(type(height), height)

#Сложение/вычитание
print(10.5 - 7)
#Произведение и деление
product = 2 * 5
print(product)
division = 21/5
print(type(division), division)
#Целочисленное деление
number = 21//5
print(type(number), number)
#Взятие остатка от деления
rest = 21.5%5
print(type(rest), rest)
#Возведение в степень
power = 2 ** (4/3)
print(type(power), power)

#Приоритетность
print(((4 + 16)*5)/10)


my_age = int(height)
print(type(my_age), my_age)


my_age_str = int(str(my_age))
print(type(my_age_str), my_age_str)

#height --> float, int(height) --> int, my_age --> str

#type - ключевое слово, которое позволяет нам посмотреть класс переменной

#int - integer - целочисленный тип данных (1,2,3, 45)
#str - string - строка
#float - нецелочисленное
#bool - boolean - логическая переменная

weather_is_good = True
print(weather_is_good)

variable = 0
variable = bool(variable)
print(variable)

num1 = 1
num2 = 1
print(num1 != num2)


#НОВОЕ ДЛЯ ДЗ
#Строки можно "склеивать" с помощью "+":
name = "Dima"
age = 21
print("Вас зовут " + name + " и Вам " + str(age) " год.")
#Печатает: Вас зовут Dima и Вам 21 год.

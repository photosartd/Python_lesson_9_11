list1 = [1, "Dima", 7.1]
#list2 = list('Dima')
print(list1)
print(list1[0:10])
# str1 = "Dima"
# print(str1[0])
# matrix = [
#     [0,1,2],
#     [3,4,5],
#     [6,7,8]
# ]
# print(matrix*2)
number_list = [4,7,3,8,4]
#Добавление элемента в конец
number_list.append("Weather")
number_list.append(100)
print(number_list)
#Добавлять по индексу
number_list.insert(0, "Hi")
print(number_list)
#Удаление элемента
number_list.remove('Hi')
print(number_list)
#Удаление элемента по индексу
number_list.pop(6)
print(number_list)
#Копирование
new_list = number_list[0:2].copy()
print(new_list)


days_list = [4,2,6,7,5,1,3]
days_list.sort()
letters_list = ['z', 'a', 'H', 'A']
letters_list.sort()
print(letters_list)

new_numbered_list = []
for i in range(4,15):
    if (i % 2 == 0):
        new_numbered_list.append(i)

print(new_numbered_list)

b = [3*i for i in range(4,15) if i % 2 == 0]
print(b)

#Перебор (итерация) списка
for element in b:
    print(element)

b[0] = 100
print(b)

#Кортеж
c = (1,2,3,4)
print(c)
print(c)
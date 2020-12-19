def list_define():
    my_list = []
    for i in range(10):
        num = int(input("Введите число: "))
        my_list.append(num)
    return my_list

#Нахождение максимума
def find_max_in_list():
    my_list = list_define()
    max_elem = my_list[0]
    for i in range(1, len(my_list)):
        if max_elem < my_list[i]:
            max_elem = my_list[i]
    return max_elem

#2 variant
def find_max_in_list_2():
    my_list = list_define()
    my_list = sorted(my_list)
    return my_list[len(my_list) - 1]


max_number_in_list = find_max_in_list_2()
print(max_number_in_list)
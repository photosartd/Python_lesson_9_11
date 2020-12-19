#Задание словарей - хэш-таблицы (Java - HashMap)
d = {'a':1, 'b':2, 'c':3, 4:10, "Hi": "How are you?"}

d1 = dict.fromkeys(['a', 'b', 'c'])

d2 = {i: i**2 for i in range(1, 20, 3)}

#print(list(d.items())[0][1])

#print(list(d.values()))

d3 = d1.copy()
d3['a'] = 100

# for key, value in d.items():
#     print(key, value)

def list_to_dict(my_list):
    dictionary = {}
    for i in my_list:
        dictionary[i] = i
    return dictionary

my_list = [4,7,2,8,5,3]
my_dict = list_to_dict(my_list)
print(my_dict)

#sets
my_set = {'Hello', 'World', 100, 'a', 'World'}
print(my_set)
my_set1 = set('Hello')
print(my_set1)
print("Hello" in my_set)

set1 = {1,2,3}
set2 = {1,2,3,4}
print(set2.issubset(set1))
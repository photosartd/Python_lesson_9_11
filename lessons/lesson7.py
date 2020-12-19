my_str = "Hello World"
my_name = " my Name is Dima"
#         01                         27
# 28
#length - длина
str_len = len(my_str)
H_name = my_str[0]
new_str = my_str*4
email = "dmitry.trofimow2011@gmail.com"
provider = "@gmail.com"
#print(email.find(provider, 19, len(email)))
number_string = "12345"

#[w, a, r, r+]
# f = open("try_test.txt", "a")
# f.write("\nWorld\n My name is Dima\n Im 21 years old")
# f.close()

file2 = open("weather.txt", "r+")
#Местонахождение до чтения
print(file2.tell())
print(file2.read())
#После чтения
print(file2.tell())
file2.seek(0)
print(file2.readline())
print(file2.readline())
file2.close()
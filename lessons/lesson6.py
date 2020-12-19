#У нас есть 4 поля, которые нужно заполнить: Имя, Фамилия, Возраст, Email
def enter_age():
    #Запросить возраст
    #Если введён не возраст (не число), должны это обработать
    while True:
        try:
            age = int(input("Enter your age: "))
        except ValueError:
            continue
        else:
            break
    return age

def enter_name():
    name = input("Enter your name: ")
    #Перевод всей строки в нижний регистр
    name = name.lower().capitalize()
    return name

def enter_surname():
    surname = input("Enter your surname: ")
    surname = surname.lower().capitalize()
    return surname


def enter_all_credentials():
    age = enter_age()
    name = enter_name()
    surname = enter_surname()
    return age, name, surname

#print(enter_all_credentials())
str1 = "dmitry.trofimow2011@gmail.com"
pattern = "@gmail.com"
if (str1.endswith(pattern)):
    print(str1)
else:
    print("This is not email")
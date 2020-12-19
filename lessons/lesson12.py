import argparse

#Нам нужно по ключу (имя) хранить значение (телефон)
book = {"Nastya": 89993456745, "Andrey": 89000001122, "Sasha": 89105673456}

parser = argparse.ArgumentParser(description="Telephone book")
parser.add_argument('-a', '--add', dest="param1")
parser.add_argument('-d', '--delete', dest="param2")
parser.add_argument('-a', '--show', dest="param3", default='all')

args = parser.parse_args()

#Формат запуска: python <path_to_file> --add "Katya:89005006878"
if args.param1:
    name, t_number = args.param1.split(":")
    #Если имени нет в книге - создаём, если уже есть - обновляем телефон
    if name in book:
        book[name] = [book.get(name), int(t_number)]
        print("Контакт с именем ", name, " обновлён")
        print(name, ":", book[name])
    else:
        book[name] = int(t_number)
        print("Контакт с именем ", name, " добавлен")
        print(name, ":", book[name])
import argparse
book = {"Masha": 89778881539, "Pasha": 89778081476, "Natasha": 89771231536}

parser = argparse.ArgumentParser(description='Telephon book')
parser.add_argument('-a', "--add", dest="param1")
parser.add_argument('-d', "--delete", dest="param2")
parser.add_argument('-s', "--show", dest="param3", default="all")

args = parser.parse_args()
# print(args)

# Формат запуска  python путь_к_файлу --add "Katya:81234567"
if args.param1:
    name, tele = args.param1.split(":")
    if name in book:
        book[name] = [book.get(name), int(tele)]
        print("Контакт с именем ", name, " обновлен")
        print(name, ":", book[name])
    else:
        book[name] = int(tele)
        print("Контакт с именем ", name, " добавлен")
        print(name, ":", book[name])

if args.param2:
    # if args.param2 == "all":
    #     book.clear()
    #     print("Книга очищена")
    if (args.param2 in book):
        book.pop(args.param2)
        print("Контакт с именем ", args.param2, " удален")
        print(book)
    else:
        print("Контакта с таким именем не существует")

if args.param3:
    if args.param3 == "all":
        print(book)
    elif (args.param3 in book):
        print(args.param3, ":", book.get(args.param3))
    else:
        print("Контакта с таким именем не существует")


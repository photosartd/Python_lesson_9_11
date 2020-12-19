def dict_with_numbers(string):
    my_dict = {}
    for letter in string:
        if letter in my_dict:
            my_dict[letter] += 1
        else:
            my_dict[letter] = 1
    return my_dict

print(dict_with_numbers('Моя хорошая собака'))
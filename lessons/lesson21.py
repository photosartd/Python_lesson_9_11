import random

def give_me_color():
    color = []
    for i in range(3):
        color.append(random.randint(0,255))
    return color

print(give_me_color())
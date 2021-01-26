class Car:
    width = 2
    def __init__(self, name, age, model):
        self.name = name
        self.age = age
        self.model = model
        self.probeg = 0

    def get_probeg(self):
        print(self.probeg)

    def set_probeg(self, value):
        self.probeg = value

    


merc = Car("Merc", 1, "GLC")
merc.get_probeg()
Car.get_probeg(merc)

class Math1:
    @staticmethod
    def sqr(number):
        return number * number

    @staticmethod
    def cube(number):
        return number * number * number

print(Math1.sqr(2))

#В staticmethod мы НЕ используем ОБЪЕКТЫ (ЭКЗЕМПЛЯРЫ), мы обращаемся к классу

class Parikm:
    @staticmethod
    def make_hairstyle(person):
        print("Bzzzh... Hairstyle is ready!")
        print(person.get_name() + " must pay!")

class Person:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

dima = Person("Dima")
Parikm.make_hairstyle(dima)

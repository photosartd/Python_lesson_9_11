class Restaurant():
    def __init__(self, name, type): 
        self.restaurant_name=name
        self.cuisine_type=type
    def describe_restaurant(self):
        print("Shaurma - " + self.restaurant_name)
        print("Voronej - " + self.cuisine_type)
    def open_restaurant(self):
        print("Ресторан открыт с 24:00\n")

restaurant = Restaurant("Фаст фуд","Ресторан")
restaurant.describe_restaurant()
restaurant.open_restaurant()

class Restaurant():
    def __init__(self, name, type): 
        self.restaurant_name=name
        self.cuisine_type=type
    def describe_restaurant(self):
        print("Doner ot Stalina - " + self.restaurant_name)
        print("Socoladnisa - " + self.cuisine_type)
    def open_restaurant(self):
        print("Ресторан открыт с 05:00\n")

restaurant = Restaurant("Фаст фуд","Кафе")
restaurant.describe_restaurant()
restaurant.open_restaurant()

class Restaurant():
    def __init__(self, name, type): 
        self.restaurant_name=name
        self.cuisine_type=type
    def describe_restaurant(self):
        print("Vkusno - " + 
    self.restaurant_name)
        print("Bulba - " + self.cuisine_type)
    def open_restaurant(self):
        print("Ресторан открыт с 9:00\n")

restaurant = Restaurant("Домашняя кухня","Беларусская кухня")
restaurant.describe_restaurant()
restaurant.open_restaurant()





 #class User():     
       # def __init__(self, first_name, last_name):
        #    self.first_name = first_name
       #     self.last_name = last_name

        #def describe_user(self):
       #     print('Name: ' + self.first_name)
       #     print('Surname: ' + self.last_name)

        #def great_user(self):
        #    full_name = self.first_name + ' ' + self.last_name
        #    print('Hello, ' + full_name + '!')
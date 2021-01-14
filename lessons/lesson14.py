class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name
        self.type = cuisine_type
    
    def describe_restaurant(self):
        print(self.name)
        print(self.type)
    
    def open_rastaurant(self):
        print("Restaurant is open")

    
class User:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
    
    def describe_user(self):
        print("Hi! My name is " + self.first_name + " " +
        self.last_name + ". Im a " + self.sex + " and " + 
        self.age + " years old.")

    def greet_user(self):
        print("Hi " + self.first_name + " " + self.last_name + "!")

dima = User("Dmitry", "Trofimov", "21", "boy")
dima.describe_user()

    
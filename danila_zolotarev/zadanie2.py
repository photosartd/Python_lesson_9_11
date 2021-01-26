class User():
    first_name = "John"
    last_name = "Wilson"
    age = 45
    height = 185
    weight = 90
    def describe_user(self):
        print(self.first_name)
        print(self.last_name)
        print(self.age)
        print(self.height)
        print(self.weight)
    def greet_user(self):
        print("Здравствуйте,", self.first_name)

user = User()
user.describe_user()
user.greet_user()




class Restaurant():
    def __init__(self, name, type):
        self.restaurant_name = name
        self.restaurant_type = type

    def open_restaurant(self):
        print('Ресторан открыт!')


restfran = Restaurant('Жан-Жак', 'Французская кухня')
print(restfran.restaurant_name)
print(restfran.restaurant_type)
restfran.open_restaurant()

restchin = Restaurant('Bruce lee', 'Китайская кухня')
print(restchin.restaurant_name)
print(restchin.restaurant_type)
restchin.open_restaurant()

restruss = Restaurant('Матрешка', 'Русская кухня')
print(restruss.restaurant_name)
print(restruss.restaurant_type)
restruss.open_restaurant()
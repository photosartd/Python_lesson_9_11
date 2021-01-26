import math
#class Point
class Point:
    def __init__(self, _x, _y):
        self.__x = _x
        self.__y = _y

    #getter (get  - получать)
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        print("Cant change this value")

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        print("Cant change this value")

    #Переопределили метод строкового представления объекта класса
    def __str__(self):
        return "This point is: x: " + str(self.__x) + ", y: " + str(self.__y)

    def __add__(self, other):
        return Point(self.__x + other.__x, self.__y + other.__y)

    def __eq__(self, other):
        return (self.__x == other.x) and (self.__y == other.y)

    #метод получения расстояния (Евклидова) между точками
    #pow - возведение в степень
    @staticmethod
    def distance(p1, p2):
        x_dist = p1.x - p2.x
        y_dist = p1.y - p2.y
        return math.sqrt(math.pow(x_dist, 2) + math.pow(y_dist, 2))


class Figure:
    def __init__(self, center):
        self.__center = center
    
    def area(self):
        print("Cant calculate area of the abstract figure")

    def perimeter(self):
        print("Cant calculate perimeter of the abstract figure")
    
    def contains(self, point):
        print("Cant say if this point is inside this figure")

class Rectangle(Figure):
    def __init__(self, left_down_point, right_top_point):
        self.__left_down = left_down_point
        self.__right_top = right_top_point

    @property
    def left_down_point(self):
        return self.__left_down
    
    @property
    def right_top_point(self):
        return self.__right_top

    def area(self):
        one_side = self.__right_top.x - self.__left_down.x
        second_side = self.__right_top.y - self.__left_down.y
        return one_side * second_side

rect = Rectangle(Point(0,0), Point(5,3))
print(rect.area())
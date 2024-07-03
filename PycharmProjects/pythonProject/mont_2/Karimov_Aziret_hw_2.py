class Figure:
    def __init__(self):
        pass

    unit = 'cm'

    def calculate_area(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        area = self.__side_length ** 2
        return area

    def info(self):
        return f'Square side length: {self.__side_length}, area: {self.__side_length ** 2}'


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def info(self):
        return f'Rectangle length: {self.__length}, width: {self.__width}, area: {self.__length * self.__width}'

    def calculate_area(self):
        area = self.__length * self.__width
        return area


figures = [Square(5), Square(7), Rectangle(5, 8), Rectangle(3, 5), Rectangle(8, 12)]

for i in figures:
    print(i.info())

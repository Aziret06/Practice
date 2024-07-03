class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'{self.__name} {self.__age}'

# print(__name__)
if __name__ == '__main__':
    person = Person('John', 23)
    print(person)

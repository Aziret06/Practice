
class Contact:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

    @property
    def city(self):
        return self.__city

    @property
    def street(self):
        return self.__street


class Animal:
    def __init__(self, name, age, contact):
        self.__name = name
        self.__age = age
        if type(contact) == Contact:
            self.__contact = contact
        else:
            raise ValueError('Contact must be of type Contact')
        self.__was_born()

    def __was_born(self):
        print(f"Animal {self.__name} was born")

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if type(age) == int and age >= 0:
            self.__age = age
        else:
            raise ValueError('Age must be a positive number')

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    @property
    def contact(self):
        return self.__contact

    def info(self):
        return (f'{self.__name} is {self.__age} years old. Birth year is {2024 - self.__age}. '
                f'\nContact Info: {self.__contact.city}, '
                f'{self.__contact.street} {self.__contact.number}')

    def speak(self):
        pass


class Cat(Animal):
    def __init__(self, name, age, contact):
        super(Cat, self).__init__(name, age, contact)

    def speak(self):
        print('Meow')


class Fish(Animal):
    def __init__(self, name, age, contact):
        super(Fish, self).__init__(name, age, contact)


class Dog(Animal):
    def __init__(self, name, age, commands, contact):
        super(Dog, self).__init__(name, age, contact)
        self.__commands = commands

    def speak(self):
        print('Woof')

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        self.__commands = value

    def info(self):
        return super().info() + f'\nCommands: {self.__commands}'


class FightingDog(Dog):
    def __init__(self, name, age, commands, wins, contact):
        super(FightingDog, self).__init__(name, age, commands, contact)
        self.__wins = wins

    def speak(self):
        print('Rrrrrr woof')

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value):
        self.__wins = value

    def info(self):
        return super().info() + f'\nWins: {self.__wins}'


# some_animal = Animal('Anim', 2)
# # some_animal.__age = -4
# some_animal.set_age(5)
# print(some_animal.get_name())
# print(some_animal.info())

contact_1 = Contact('Bishkek', 'Isanova', 25)

cat = Cat('Tom', 3, contact_1)
# print(cat.info())

dog = Dog('Snooppy', 5, ['sit', 'run'], contact_1)
dog.commands = ['sit', 'run', 'bark']
# print(dog.commands)
# print(dog.info())

# contact_2 = Contact('Osh', 'Lenina', 2)
#         a = b
fighting_dog = FightingDog('Reks', 1, ['fight'], 15,
                           Contact('Osh', 'Lenina', 2))
# print(fighting_dog.info())

# contact_1.number = 100
# print(cat.info())
# fighting_dog.contact.number = 33
# print(fighting_dog.info())

fish = Fish('Nemo', 2, contact_1)

animals = [cat, fish, dog, fighting_dog]
for animal in animals:
    print(animal.info())
    animal.speak()

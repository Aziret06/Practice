# OOП 1: Основы ООП, Создание первых классов,
# Атрибуты и Методы классов, Принцип ООП - Наследование.

class Transport:
    def __init__(self, the_model, the_year, the_color):
        self.model = the_model
        self.year = the_year
        self.color = the_color

    def change_color(self, new_color):
        self.color = new_color


class Plane(Transport):
    def __init__(self, the_model, the_year, the_color):
        # constructor matching
        super().__init__(the_model, the_year, the_color)


class Car(Transport):
    # class attributes
    counter = 0

    # constructor                   # parameters
    def __init__(self, the_model, the_year, the_color, penalties=0):
        # attributes / fields
        super().__init__(the_model, the_year, the_color)
        self.penalties = penalties
        Car.counter += 1

    # methods
    def drive(self, city, speed):
        print(f'Car {self.model} is driving to {city} in {speed}km/h')

    def signal(self, number_of_times, sound):
        print(f'Car {self.model} signaling: ')
        while number_of_times > 0:
            print(sound)
            number_of_times -= 1


class Truck(Car):
    counter = 0

    def __init__(self, the_model, the_year, the_color, penalties=0, load_capacity=0):
        super().__init__(the_model, the_year, the_color, penalties)
        self.load_capacity = load_capacity
        Truck.counter += 1

    def load_cargo(self, weight, type_of_products):
        if weight > self.load_capacity:
            print(f'You can not load more than {self.load_capacity} kg.')
        else:
            print(f'You successfully loaded the cargo of {type_of_products} ({weight} kg.).')


print(f'Factory CAR produced: {Car.counter} cars.')

number = 9
honda_car = Car('Honda Fit', 2020, 'blue')
print(number)
print(honda_car)
print(f'MODEL: {honda_car.model} YEAR: {honda_car.year} COLOR: {honda_car.color}'
      f' PENALTIES: {honda_car.penalties}')

bmw_car = Car(the_color='red', the_model='BMW X6', the_year=2019, penalties=900)
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} COLOR: {bmw_car.color}'
      f' PENALTIES: {bmw_car.penalties}')
# bmw_car.color = 'yellow'
bmw_car.change_color('yellow')
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} NEW COLOR: {bmw_car.color}'
      f' PENALTIES: {bmw_car.penalties}')

bmw_car.drive('Osh', 100)
honda_car.drive('Kant', 80)
honda_car.signal(3, 'beep')
bmw_car.drive('Batken', 90)


boeing_plane = Plane('Boeing 747', 2022, 'white')
print(f'MODEL: {boeing_plane.model} YEAR: {boeing_plane.year} COLOR: {boeing_plane.color}')

volvo_truck = Truck('Volvo D988', 2021, 'orange',
                    1000, 35000)
print(f'MODEL: {volvo_truck.model} YEAR: {volvo_truck.year} COLOR: {volvo_truck.color}'
      f' PENALTIES: {volvo_truck.penalties} LOAD CAPACITY: {volvo_truck.load_capacity}')
volvo_truck.load_cargo(40000, 'potatoes')
volvo_truck.load_cargo(20000, 'tomatoes')
volvo_truck.drive('Tokmok', 90)


print(f'Factory CAR produced: {Car.counter} cars.')
print(f'Factory TRUCK produced: {Truck.counter} trucks.')


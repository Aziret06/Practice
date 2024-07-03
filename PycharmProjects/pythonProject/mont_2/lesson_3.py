from enum import Enum


class Color(Enum):
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'


class Drawable:
    @staticmethod
    def draw(emoji):
        print(emoji)


class MusicPlayable:  # class mixin
    # def __init__(self):
    #     pass

    @staticmethod
    def play_music(song):
        print('Playing ' + song)

    @staticmethod
    def stop_music():
        print('Music stopped')


class SmartPhone(MusicPlayable, Drawable):
    pass


class Car(MusicPlayable, Drawable):
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        if type(color) == Color:
            self.__color = color

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def drive(self):
        print(f'Car {self.__model} is driving')

    def __str__(self):
        return (f'Model: {self.__model}, Year: {self.__year}, '
                f'Color: {self.__color.value}{self.__color.name}' + '\033[0m')

    def __gt__(self, other):
        return self.__year > other.__year

    def __lt__(self, other):
        return self.__year < other.__year

    def __eq__(self, other):
        return self.__year == other.__year

    def __ne__(self, other):
        return self.__year != other.__year

    def __le__(self, other):
        return self.__year <= other.__year

    def __ge__(self, other):
        return self.__year >= other.__year


class FuelCar(Car):
    __total_fuel = 0

    @staticmethod
    def get_fuel_type():
        return 'AI 95'

    @classmethod
    def buy_fuel(cls, amount):
        cls.__total_fuel += amount

    @classmethod
    def get_total_fuel(cls):
        return cls.__total_fuel

    def __init__(self, model, year, color, fuel_bank):
        # super().__init__(model, year, color)
        # super(FuelCar, self).__init__(model, year, color)
        Car.__init__(self, model, year, color)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel -= self.__fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    @fuel_bank.setter
    def fuel_bank(self, value):
        self.__fuel_bank = value

    def fill_fuel(self, amount):
        print(f'Fuel filled - {amount} litters.')

    def drive(self):
        print(f'Car {self.model} is driving by fuel')

    def __str__(self):
        return Car.__str__(self) + f', Fuel Bank: {self.__fuel_bank}'

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank


class ElectricCar(Car):
    def __init__(self, model, year, color, battery):
        Car.__init__(self, model, year, color)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f'Car {self.model} is driving by electricity')

    def charge_battery(self):
        print('Charging battery')

    def __str__(self):
        return Car.__str__(self) + f', Battery: {self.__battery}'


class HybridCar(ElectricCar, FuelCar):
    def __init__(self, model, year, color, fuel_bank, battery):
        FuelCar.__init__(self, model, year, color, fuel_bank)
        ElectricCar.__init__(self, model, year, color, battery)

    def __str__(self):
        return ElectricCar.__str__(self) + f', Fuel Bank: {self.fuel_bank}'


# some_car = Car('Ford Focus', '2009', 'Black')
# print(some_car)

FuelCar.buy_fuel(1000)
print(f'Factory FUEL_CAR has {FuelCar.get_total_fuel()} '
      f'litters ({FuelCar.get_fuel_type()}).')

mustang_car = FuelCar('Ford Mustang', '2019', Color.RED, 85)
print(mustang_car)

tesla_car = ElectricCar('Tesla Model X', '2022', Color.GREEN, 25000)
print(tesla_car)

avalon_car = HybridCar('Toyota Avalon', '2021',
                       Color.BLUE, 70, 15000)
print(avalon_car)
avalon_car.drive()

print(HybridCar.mro())

number_1, number_2 = 4, 10
print(f'Number 1 is greater than Number 2: {number_1 > number_2}')
print(f'Number 1 is less than Number 2: {number_1 < number_2}')
print(f'Mustang is better than Avalon: {mustang_car > avalon_car}')
print(f'Tesla is better than Mustang: {tesla_car > mustang_car}')
print(f'Tesla is the same with Mustang: {tesla_car == mustang_car}')

print(number_1 + number_2)
print(mustang_car + avalon_car)

# FuelCar.total_fuel -= 100
print(f'Factory FUEL_CAR has {FuelCar.get_total_fuel()} '
      f'litters ({FuelCar.get_fuel_type()}).')

mustang_car.play_music('Best Song')
mustang_car.draw('🏎️')

samsung = SmartPhone()
samsung.play_music('Song 1')
samsung.draw('📱')

if tesla_car.model == 'Tesla Model x':
    print('This car is cool')

if tesla_car.color == Color.GREEN:
    print('This car is beautiful')

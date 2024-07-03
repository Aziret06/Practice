# import random импортирование всего модуля
from random import randint, choice as random_element  # alias
import calculator as calc
from utilities.templates import Person
from termcolor import cprint
from emoji import emojize
from decouple import config

print(randint(1, 6))
print(random_element(['apple', 'pear', 'orange', 'banana']))

print(calc.add(5, 7))

my_friend = Person('Jim', 20)
print(my_friend)

cprint("Hello, World!", "green", "on_red")
print(emojize('Python is :thumbs_up:'))

print(config('SECRET_KEY'))

commented = config('COMMENTED', default=0, cast=int)
print(commented * 2)

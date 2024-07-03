# Функции (ч. 1): виды параметров, возвращение данных, виды аргументов.
# DRY - don't repeat yourself
# def - define
# pass - приглушение функции

""""схема функций"""

# определение наименование(параметры):
#     тело функции
#     возвращение результата
#
# вызов функции
# наименование(аргуменнты)


# name=required positional argument; surname=non-required positional argument
# def get_data(name, surname='incognito'):
#     print(f'name: {name} surname: {surname}')
#
#
# get_data("mirbek", "atabekov")  # required positional arguments
# get_data(surname="alba", name="jessica")  # keyword arguments
# get_data(surname="puyol", name="carles")  # keyword arguments
# get_data('floyd')

# letters_count = len('geeks')
# print(letters_count + 5)
#
#
# def len1(iterable):
#     counter = 0
#     for i in iterable:
#         counter += 1
#     return counter
#
#
# letters_count1 = len1('words')
# print(letters_count1)

# print(len.__doc__)
# print(help(len))


"""Функция принимает ширину и длину, затем возвращает площадь."""

# def get_square(length: int, width: int) -> int:
#     return width * length


# square_2 = get_square(7, 5)
# print(square_2)
#
# square_victory = get_square(550, 300)
# print(square_victory)

# print(help(get_square))
# print(get_square.__doc__)

# width = 5
# length = 7
# square_2 = width * length
# print(square_2)

# width = 300
# length = 550
# square_victory = width * length
# print(square_victory)

# Создать два пустых списка letters и numbers
# Пройтись циклом for по кортежу data_tuple, добавить все строки в список letters, а всё остальное в numbers.
# Из списка numbers удалить число 6.13 и переместить True в конец списка letters, затем вставить число 2 между 3 и 1
# Отсортировать numbers, реверсировать letters и изменить пару букв в letters.
# Измените список numbers в список квадратов своих же чисел
# Преобразовать списки numbers и letters в кортежи

# кортеж letters должен выглядеть так:   (True, 'G', 'e', 'e', 'k', 'T', 'e', 'c', 'h')
# кортеж numbers должен выглядеть так:   (1, 4, 9)

data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

for sign in data_tuple:
    if type(sign) == str:
        letters.append(sign)
    else:
        numbers.append(sign)

numbers.remove(6.13)
deleted = numbers.pop(0)
letters.append(deleted)
numbers.insert(1, 2)
numbers.sort()
letters.reverse()
letters[1] = 'G'
letters[-2] = 'c'
#
numbers_square = [number ** 2 for number in numbers]

numbers = tuple(numbers_square)
letters = tuple(letters)

print(letters)
print(numbers)

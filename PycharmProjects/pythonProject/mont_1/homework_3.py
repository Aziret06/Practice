# Счетчик гласных и согласных букв
# Программа должна работать в цикле while с возможностью выхода (break)
# Запрашивать у пользователя любое слово на латинице или кириллице
# Считывать строчные и прописные буквы (большие и маленькие)
# Вывести общее количество букв в данном слове
# Вывести количество согласных и гласных букв
# Вывести процентное соотношение гласных и согласных букв  в дробном числе (до двух цифр после точки)

print('Добро пожаловать в "Счетчик гласных и согласных букв"')

while True:

    word = input('Введите слово на латинице или кириллице: ').lower()
    if word == 'stop' or word == 'стоп':
        print('Выход')
        break

    letters = 0
    count_vowels = 0
    count_consonant = 0

    vowels = 'a', 'e', 'y', 'u', 'o', 'i', 'ё', 'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю'

    for letter in word:
        letters += 1
        if letter in vowels:
            count_vowels += 1
        else:
            count_consonant += 1

    vowels_percent = round(count_vowels * 100 / letters, 2)
    consonant_percent = round(count_consonant * 100 / letters, 2)

    print(f'Букв: {letters}')
    print(f'Гласных: {count_vowels}  или {vowels_percent}%')
    print(f'Соласных: {count_consonant} или {consonant_percent}%')

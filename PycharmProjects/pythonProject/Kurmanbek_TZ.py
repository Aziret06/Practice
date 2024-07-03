while True:
    try:
        n = int(input("Введите требуемый опыт работы: "))

        experience_list = list(map(int, input("Введите список опыта работы кандидатов через пробел: ").split()))

        indexes = []
        for i in range(len(experience_list)):
            if experience_list[i] >= n:
                indexes.append(i)

        print("Индексы подходящих кандидатов:", indexes)
        break
    except ValueError:
        print('Неправильный ввод! Вводите только числа!')

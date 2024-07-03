print("Добро пожаловать!")
while True:
    try:
        to_continue = input('Хотите продолжить? (да или нет) ').lower()

        if to_continue == 'да':

            date = input('Введите день и месяц рождения (например: 31.01, 31-01, 31/01): ')
            day = int(date[:2])
            month = int(date[3:])

            # можно и так сделать:
            # day = int(input("Введите день рождения: "))
            # month = int(input("Введите месяц рождения (Например: 01, 11 и т.п.): "))

            if (month == 3 and 21 <= day <= 31) or (month == 4 and 1 <= day <= 20):
                print("Ваш знак зодиака: Овен.")
            elif (month == 4 and 21 <= day <= 30) or (month == 5 and 1 <= day <= 21):
                print("Ваш знак зодиака: Телец.")
            elif (month == 5 and 22 <= day <= 31) or (month == 6 and 1 <= day <= 21):
                print("Ваш знак зодиака: Близнецы.")
            elif (month == 6 and 22 <= day <= 30) or (month == 7 and 1 <= day <= 22):
                print("Ваш знак зодиака: Рак.")
            elif (month == 7 and 23 <= day <= 31) or (month == 8 and 1 <= day <= 21):
                print("Ваш знак зодиака: Лев.")
            elif (month == 8 and 22 <= day <= 31) or (month == 9 and 1 <= day <= 23):
                print("Ваш знак зодиака: Дева.")
            elif (month == 9 and 24 <= day <= 30) or (month == 10 and 1 <= day <= 23):
                print("Ваш знак зодиака: Весы.")
            elif (month == 10 and 24 <= day <= 31) or (month == 11 and 1 <= day <= 22):
                print("Ваш знак зодиака: Скорпион.")
            elif (month == 11 and 23 <= day <= 30) or (month == 12 and 1 <= day <= 22):
                print("Ваш знак зодиака: Стрелец.")
            elif (month == 12 and 23 <= day <= 31) or (month == 1 and 1 <= day <= 20):
                print("Ваш знак зодиака: Козерог.")
            elif (month == 1 and 21 <= day <= 31) or (month == 2 and 1 <= day <= 19):
                print("Ваш знак зодиака: Водолей.")
            elif (month == 2 and 20 <= day <= 29) or (month == 3 and 1 <= day <= 20):
                print("Ваш знак зодиака: Рыбы.")
            else:
                print("(0.04, 32.05, 11.00, 03.14) считается неправильно введенной датой! Попробуйте снова.")

        elif to_continue == 'нет':
            print('До свидания!')
            break
        else:
            print('Неверный ввод!')
    except ValueError:
        print('Вводите только числа, как на примере!')

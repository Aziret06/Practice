# Написать программу знаков зодиака.
# Программа должна запрашивать у пользователя день и месяц рождения,
# затем выводить на экран соответствующий знак зодиака.
# В случае неверного ввода дней и месяцев, вывести на экран подсказку корректного ввода.

for i in range(1, 13):
    print(i)

# counter = 0
# while counter < 12:
#     counter += 1
#     print(counter)
#
#     day = int(input("Введите день рождения: "))
#
#     if day == 0:
#         print('BYE!')
#         break
#
#     month = input("Введите месяц рождения (Например: май, январь и т.п.): ").lower()

    date = input('Введите день и месяц (Например: д.м, д-м, д/м): ')
    day = int(date[:2])
    month = int(date[3:])


    if (month == 3 and 21 <= day <= 31) or (month == 4 and 1 <= day <= 20):
        print("Овен")
    elif (month == 4 and 21 <= day <= 30) or (month == 5 and 1 <= day <= 21):
        print("Телец")
    elif (month == 5 and 22 <= day <= 31) or (month == 6 and 1 <= day <= 21):
        print("Близнецы")
    elif (month == 6 and 22 <= day <= 30) or (month == 7 and 1 <= day <= 22):
        print("Рак")
    elif (month == 7 and 23 <= day <= 31) or (month == 8 and 1 <= day <= 21):
        print("Лев")
    elif (month == 8 and 22 <= day <= 31) or (month == 9 and 1 <= day <= 23):
        print("Дева")
    elif (month == 9 and 24 <= day <= 30) or (month == 10 and 1 <= day <= 23):
        print("Весы")
    elif (month == 10 and 24 <= day <= 31) or (month == 11 and 1 <= day <= 22):
        print("Скорпион")
    elif (month == 11 and 23 <= day <= 30) or (month == 12 and 1 <= day <= 22):
        print("Стрелец")
    elif (month == 12 and 23 <= day <= 31) or (month == 1 and 1 <= day <= 20):
        print("Козерог")
    elif (month == 1 and 21 <= day <= 31) or (month == 2 and 1 <= day <= 19):
        print("Водолей")
    elif (month == 2 and 20 <= day <= 29) or (month == 3 and 1 <= day <= 20):
        print("Рыбы")
    else:
        print("(0.04, 32.05, 0 апрель, 32 май) считается неправильно введенной датой! Попробуйте снова.")

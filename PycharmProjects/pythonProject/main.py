
day = int(input("Введите день рождения: "))
month = input("Введите месяц рождения (Например: май, январь и т.п.): ").lower()

if (month == "март" and 21 <= day <= 31) or (month == "апрель" and 1 <= day <= 20):
    print("Овен")
elif (month == "апрель" and 21 <= day <= 30) or (month == "май" and 1 <= day <= 21):
    print("Телец")
elif (month == "май" and 22 <= day <= 31) or (month == "июнь" and 1 <= day <= 21):
    print("Близнецы")
elif (month == "июнь" and 22 <= day <= 30) or (month == "июль" and 1 <= day <= 22):
    print("Рак")
elif (month == "июль" and 23 <= day <= 31) or (month == "август" and 1 <= day <= 21):
    print("Лев")
elif (month == "август" and 22 <= day <= 31) or (month == "сентябрь" and 1 <= day <= 23):
    print("Дева")
elif (month == "сентябрь" and 24 <= day <= 30) or (month == "октябрь" and 1 <= day <= 23):
    print("Весы")
elif (month == "октябрь" and 24 <= day <= 31) or (month == "ноябрь" and 1 <= day <= 22):
    print("Скорпион")
elif (month == "ноябрь" and 23 <= day <= 30) or (month == "декабрь" and 1 <= day <= 22):
    print("Стрелец")
elif (month == "декабрь" and 23 <= day <= 31) or (month == "январь" and 1 <= day <= 20):
    print("Козерог")
elif (month == "январь" and 21 <= day <= 31) or (month == "февраль" and 1 <= day <= 19):
    print("Водолей")
elif (month == "февраль" and 20 <= day <= 29) or (month == "март" and 1 <= day <= 20):
    print("Рыбы")
else:
    print("(0.04, 32.05, 0 апрель, 32 май) считается неправильно введенной датой! Попробуйте снова.")

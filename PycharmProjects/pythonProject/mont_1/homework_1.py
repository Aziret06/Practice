# Написать программу для вычисления расходов за неделю.
# Расход каждого дня недели должен вводиться пользователем по запросу программы (input),
# на каждый отдельный день должна быть отдельная переменная.
# Вывести общую сумму расходов.
# Вывести средний расход в день. (средний расход должен быть в дробном числе,
# округленным с одной цифрой после точки (round))
while True:

    monday = float(input("Рассход за понедельник: "))
    tuesday = float(input("Рассход за вторник: "))
    wednesday = float(input("Рассход за среду: "))
    thursday = float(input("Рассход за четверг: "))
    friday = float(input("Рассход за пятницу: "))
    saturday = float(input("Рассход за субботу: "))
    sunday = float(input("Рассход за воскресенье: "))

    total = monday + tuesday + wednesday + thursday + friday + saturday + sunday
    print(f"Общий рассход: {total}")
    average = round(total / 7, 1)
    print(f"Средний расход в день: {average}")

    if 1 <= total <= 500:
        print('Мало потратили.')
    elif 501 <= total <= 2500:
        print('Средне потратили.')
    elif total >= 2501:
        print('Много потратили.')
    else:
        print('Ничего не потратили.')

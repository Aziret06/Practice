
def scores(homeworks, tests, visits):
    try:
        if 50 <= homeworks <= 60 <= tests and visits < 6:
            discount = 'Ваша скидка: 1000'
        elif 50 <= homeworks <= 60 <= tests and visits >= 6:
            discount = 'Ваша скидка: 2000'
        elif 50 <= homeworks <= 60 and tests >= 80 and visits < 6:
            discount = 'Ваша скидка: 2000'
        elif 70 <= homeworks <= 80 and tests >= 60 and visits < 8:
            discount = 'Ваша скидка: 2000'
        elif 70 <= homeworks <= 80 <= tests and visits <= 8:
            discount = 'Ваша скидка: 3000'
        elif 70 <= homeworks <= 80 and tests >= 60 and visits >= 8:
            discount = 'Ваша скидка: 2500'
        return discount
    except:
        print('Неправильный ввод!')


print(scores(50, 60, 5))
print(scores(50, 60, 6))
print(scores(50, 60, 8))
print(scores(60, 70, 6))
print(scores(70, 80, 6))
print(scores(70, 70, 7))
print(scores(70, 70, 8))
print(scores(80, 80, 8))



word = 'python'

while True:
    try:
        index_user = int(input('Enter index: '))
        print(word[index_user])

    except IndexError:
        print('Неверный индекс!')
    except ValueError:
        print('Вводите только числа!')
#
#     except:
#         print('Ошибка!')


# date = input('Enter day and month (day.month, day-month, day/month')
# day = int(date[:2])
# month = int(date[3:])
# print(day, month)


# word = 'python'
# print(word)

"""срезы"""
# [start:stop:step]
# print(word[0:3:1])
# print(word[::2])
# print(word[::])
# print(word[::-1])

"""индекс"""
# print(word[0])
# print(word[3])
# print(word[-1])
# print(word[-2])

# try:
#     print(2 / 'hello')
# except:
#     print('Ошибка найдена!')
# finally:
#     print('Проверка завершена')

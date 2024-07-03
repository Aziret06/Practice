# list - списки (изменяется)
# tuple - кортеж (не изменяется)

# days = ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')
# amount_days = len(days)
# expenses = []
#
# for day in days:
#     expenses.append(int(input(f'Введите расход за {day.upper()}: ')))
#
# print(days)
# print(expenses)
# print(sum(expenses))
# print(sum(expenses) / amount_days)


# students = 'kairat', 'askar', 'regina', 'meerim'
# print(students)  # кортеж
# students = list(students)
# print(students)  # список из кортежа

# for num in list(range(1, 11)):
#     print(num)
# print(list(range(1, 11)))
# print(list('geeks'))

# numbers = [23, 45, 12, 78, 4]
#
# print(len(numbers))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))


students = ['chyngyz', 'omurbek', 'marsel', 'amirhan', 'aliaskar', 'chyngyz']

"""delete"""
# students = [student for student in students if 'mars' not in student]
# print(students)

# students.remove('marsel')
# students.pop(-1)
# deleted = students.pop(-1)
# print(deleted)
# del students[:2]
# print(students)

"""add"""
students.append('aslan')
# students.insert(2, 'amirhan')
# students.extend(['bekzat', 'aziret'])
# students += ['ahilles', 'arlen']
print(students)

"""edit"""
# students.sort()
# students.reverse()
# students[-1] = 'aliaskar'
# students[:3] = 'alina', 'karina'
# students[:5:2] = 'timur', 'erlan', 'urmat'

# students2 = []
# for i in students:
#     students2.append(i.title())
#
# students2 = [student.title() for student in students]
#
# print(students2)


"""схема list comprehension"""
# [object cycle]

# I=8
# students = [7, 6, 13, 15, 4, 9, 12, 8, 3, 11, 14, 10, 16, 1]


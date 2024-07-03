# словари - dict (dictionary),
# множества - set.
# {key: value}

# beshbarmak = {"мясо", "тесто", "шорпо", "лук"}
# plov = {"мясо", "рис", "морковь"}

# print(beshbarmak.difference(plov))
# print(beshbarmak.union(plov))
# print(beshbarmak.intersection(plov))
# print(beshbarmak.symmetric_difference(plov))

# numbers = [1, 2, 3, 4, 2, 1, 3, 5]
# numbers2 = {1, 2, 3, 4, 2, 1, 3, 5}

# print(type(numbers2))
# print(numbers)
# print(numbers2)


# days = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")
# data = {}

# for day in days:
#     data[day] = int(input(f'Enter expense for {day}: '))
#     print(data)

# data = {'mon': 10, 'tue': 20, 'wed': 32, 'thu': 12, 'fri': 34, 'sat': 67, 'sun': 90}

# print(data.keys())
# print(data.values())
# print(sum(data.values()))
# print(sum(data.values()) / len(data))

student = {
    'name': 'Azamat',
    'age': 20
}

# for key, value in student.items():
#     print(f'{key}: {value}')

# print(student.keys())
# print(student.values())
# print(student.items())

"""исключение ошибки ввода ключа"""
# print(student.get('nam', 'Неверный ключ!'))
# print(student.get('name', 'Неверный ключ!'))

"""add"""
student['height'] = 1.78
# student['married'] = False
# student['hobby'] = ['english', 'books', 'chess']
# student['education'] = ('school', 'college')

"""edit"""
# student['age'] = 21
# student['hobby'][0] = 'chinese'

"""delete"""
# student.pop('education')
# del student['hobby']

for i in student:
    print(f'{i}: {student[i]}')

# print(student['hobby'][1])
# print(student['name'])
# print(type(student))



# Создать два пустых списка designations и codes
# Пройтись циклом for по кортежу data, добавить наименования компаний в designations и коды в codes
# Создать словарь operators на основе списков designations и codes c помощью цикла while
# или встроенных функций dict() и zip() , где ключами будут названия компаний а значениями коды содержащиеся в множестве.
# Удалить нефункционирующие операторы из словаря operators. (Katel, Fonex)
# Добавить/Обновить к уже существующим номерам (Ошке, Меге и Билайну) пару кодов на своё усмотрение.
# В итоге вывести на экран наименования операторов и соответствующие номера в таком виде (в паре ключ-значение):

data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

designations = []
codes = []

operators = {}

for designation in data:
    if designation.isdigit():
        codes.append(designation)
    else:
        designations.append(designation)

operators = dict(zip(designations, codes))

del operators['Katel']
del operators['Fonex']

operators['O!'] = {'0705', '0700', '0500'}
operators['Megacom'] = {'0550', '0995', '0998'}
operators['Beeline'] = {'0770', '0775', '0772'}

# print(designations)
# print(codes)
for i in operators:
    print(f'{i} - {operators[i]}')

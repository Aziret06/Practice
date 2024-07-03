cash = 100
percents = 0.1
years = 5

for year in range(1, years+1):
    cash += int(cash * percents)
    print(f'{year}) {cash}')


# interable, index, item

# for number in range(1, 11):
#     print(number)

# for letter in 'Bishkek':
#     print(letter)
#
# for letter in 'Bishkek':
#     if letter == 'h':
#         break
#     print(letter)
#
# for letter in 'Bishkek':
#     if letter == 'h':
#         continue
#     print(letter)



# count_green = 0
# count_yellow = 0
# count_red = 0
# count_off = 0
#
# while True:
#     signal = input('Signal? ').lower()
#
#     if signal == 'stop':
#         print('Stop!')
#         break
#
#     if signal == 'green' or signal == 'зеленый':
#         print('GO!')
#         count_green += 1
#
#     elif signal == 'yellow' or signal == 'желтый':
#         print('WAIT!')
#         count_yellow += 1
#
#     elif signal == 'red' or signal == 'красный':
#         print('STOP!')
#         count_red += 1
#     else:
#         print("Stoplight is broken down.")
#         count_off += 1
#
# print(
#     f"red: {count_red}\n"
#     f"yellow: {count_yellow}\n"
#     f"green: {count_green}\n"
#     f"off: {count_off}"
# )


# counter = 0
#
# while counter < 200:
#     counter += 1
#     if counter % 2 == 1:
#         continue
#     print(counter)


# counter = 0
# while counter < 100:
#     print(counter)
#     if counter == 50:
#       print ('exit...')
#       brake
#     counter += 1


# n = 5
# while n > 0:
#     print(n)
#     if n == 3:
#         print('stop')
#         break
#     n -= 1


"""оператор принадлежности - in"""
# print('e' in 'geeks')
# print('w' in  'geeks')
# print(45 in range(1, 100))
# print(100 in range(1, 100))


"""операторы принадлежности"""
# number = 10
# number = number + 5
# number += 5
# number -= 3
# number *= 5
# number /= 7
# number %= 3
# number //= 2
# print(number)

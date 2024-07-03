
def nearest_number(numerals, target):
    sort = sorted(numerals, key=lambda x: abs(x - target))
    return target, sort


result = nearest_number([100, 221, 355, 49, 85], 150)
print(result)


numbers = [i for i in range(1, 11)]
print(f'Numbers: {numbers}')

filtered_numbers = tuple(filter(lambda x: x % 3 == 0, numbers))
print(f'Numbers that divide by three: {filtered_numbers}')

mapped_numbers = list(map(lambda x: x**2, numbers))
print(f'Number squares: {mapped_numbers}')


count_green = 0
count_yellow = 0
count_red = 0
count_off = 0

while True:
    signal = input('Signal? ').lower()

    if signal == 'stop':
        print('Stop!')
        break

    if signal == 'green' or signal == 'зеленый':
        print('GO!')
        count_green += 1

    elif signal == 'yellow' or signal == 'желтый':
        print('WAIT!')
        count_yellow += 1

    elif signal == 'red' or signal == 'красный':
        print('STOP!')
        count_red += 1
    else:
        print("Stoplight is broken down.")
        count_off += 1

print(
    f"red: {count_red}\n"
    f"yellow: {count_yellow}\n"
    f"green: {count_green}\n"
    f"off: {count_off}"
)

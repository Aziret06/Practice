class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        print(f'Выполняется арифмитическое действие с cpu и memory.')

    def __str__(self):
        return f'Компьютер CPU: {self.cpu}, MEMORY: {self.memory}'

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __lt__(self, other):
        return self.memory < other.__memory

    def __eq__(self, other):
        return self.memory == other.__memory

    def __ne__(self, other):
        return self.memory != other.__memory

    def __le__(self, other):
        return self.memory <= other.__memory

    def __ge__(self, other):
        return self.memory >= other.__memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if sim_card_number == 1:
            print(f'Идетзвонок на номер: {call_to_number} с сим-карты {sim_card_number} - O!')
        elif sim_card_number == 2:
            print(f'Идетзвонок на номер: {call_to_number} с сим-карты {sim_card_number} - Megacom')
        else:
            print('Нет такой сим-карты.')

    def __str__(self):
        return f'Телефон со списком контактов: {self.sim_cards_list}'


class SmartPhone(Phone, Computer):
    def __init__(self, sim_cards_list, cpu, memory):
        Phone.__init__(self, sim_cards_list)
        Computer.__init__(self, cpu, memory)

    def use_gps(self, location):
        print(f'Маршрут построен от данной точки до точки "{location}" ')

    def __str__(self):
        return f'Смартфон со списком контактов: {self.sim_cards_list}, CPU: {self.cpu}, MEMORY: {self.memory}'


computer = Computer('intel core i3 на 16 гб', 512)
phone = Phone(['0706496924', '0555679459', '0779508762'])
smart_phone_1 = SmartPhone(['0555999772', '0776597562'], 'Snapdragon777 на 8 гб', 128)
smart_phone_2 = SmartPhone(['0700556698', '0550697896'], 'Snapdragon357 на 6 гб', 256)

print(computer)
print(phone)
print(smart_phone_1)
print(smart_phone_2)
computer.make_computations()
phone.call(1, '0706484946')
smart_phone_1.use_gps('ЦУМ')
smart_phone_2.use_gps('ГУМ')

print(computer > smart_phone_1)
print(computer >= smart_phone_2)
print(computer < smart_phone_1)
print(computer <= smart_phone_2)
print(computer == smart_phone_1)
print(computer != smart_phone_1)
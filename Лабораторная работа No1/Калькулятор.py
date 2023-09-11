import math

def elems(action):
    while True:
        try:
            first_elem = int(input('Введите первый элемент: '))
            second_elem = int(input('Введите второй элемент: '))
        except ValueError:
            print('Элемент не является числом.\n')
        else:
            if action == '+':
                return first_elem + second_elem
            elif action == '-':
                return first_elem - second_elem
            elif action == '*':
                return first_elem * second_elem
            elif action == '/':
                return first_elem / second_elem
            elif action == 'log':
                return math.log(first_elem, second_elem)
            elif action == '**':
                return first_elem ** second_elem


commands = ['Сложение', 'Вычитание', 'Умножение', 'Деление', 'Логарифм',
            'Возведение в N-степень', 'Округление в большую степень', 'Округление в меньшую степень']

print('Список доступных команд:', ', '.join(commands))

while True:
    choice = input('\nВыберите команду для выполения: ')
    if choice == 'Сложение':
        print('Сумма элементов:', elems('+'))
    elif choice == 'Вычитание':
        print('Разность элементов:', elems('-'))
    elif choice == 'Умножение':
        print('Произведение элементов:', elems('*'))
    elif choice == 'Деление':
        print('Частное элементов:', elems('/'))
    elif choice == 'Логарифм':
        print('Логарифм элементов:', elems('log'))
    elif choice == 'Возведение в N-степень':
        print('Степень первого числа:', elems('**'))
    elif choice == 'Округление в большую степень':
        elem = float(input('Введите элемент: '))
        print('Округлённый элемент в большую степень:', math.ceil(elem))
    elif choice == 'Округление в меньшую степень':
        elem = float(input('Введите элемент: '))
        print('Округлённый элемент в меньшую степень:', math.floor(elem))
    elif choice == 'exit':
        print('Программа завершена.')
        break
    else:
        print('Неизвестная команда, повторите заново.')
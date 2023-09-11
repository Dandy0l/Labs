print('12345 это строка')
print(12345, 'Это число\n')

print('Сложение строк:\n', '1234' + '5678')
print('Сложение чисел:\n', 1234 + 5678)

even_numbered_mass = list(num for num in range(0, 12, 2))
odd_numbered_mass = [num for num in range(1, 10, 2)]

print('\nМассив чётныйх чисел', even_numbered_mass)
print('Массив нечётныйх чисел', odd_numbered_mass)
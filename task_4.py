"""
4. Написать программу, которая генерирует
в указанных пользователем границах:
- случайное целое число;
- случайное вещественное число;
- случайный символ.

Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

import random

num_start = int(input('Введите нижнюю границу диапазона (целое число): '))
num_end = int(input('Введите верхнюю границу диапозона (целое число): '))
if num_start < num_end:
    ran_int = random.randint(num_start, num_end)
    ran_float = random.uniform(num_start, num_end)

    print(f'Случайное целое число\n'
          f'в диапазоне от {num_start} до {num_end} включительно = {ran_int}')
    print(f'Случайное вещественное число\n'
          f'в диапазоне от {num_start} до {num_end} включительно = {ran_float}')

    letter_start = input('Введите букву-начало диапазона: ')
    letter_end = input('Введите букву-конец диапазона: ')

    if ord(letter_start) < ord(letter_end):
        ran_symbol = random.randint(ord(letter_start), ord(letter_end))
        ran_symbol = chr(ran_symbol)

        print(f'Случайный символ в диапазоне\n'
              f' от {letter_start} до {letter_end} включительно = {ran_symbol}')

    else:
        print(f'Ошибка. Неправильно заданы границы диапазона:\n'
              f'второе введённое число должно быть больше первого')
else:
    print(f'Ошибка. Неправильно заданы границы диапазона:\n'
          f'второе введённое число должно быть больше первого')

"""
9. Вводятся три разных числа.
Найти, какое из них является средним
(больше одного, но меньше другого).
"""

print('Введите три разных числа.')
num1 = int(input("1-е число: "))
num2 = int(input("2-е число: "))
num3 = int(input("3-е число: "))

min_num = min(num1, num2, num3)
max_num = max(num1, num2, num3)

middle = num1 + num2 + num3 - min_num - max_num

print(f'Средним из чисел {num1}, {num2}, {num3} является {middle}.')

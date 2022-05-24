"""
5. Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят
и сколько между ними находится букв.
"""

letter1 = input('Введите первую букву: ').upper()
letter2 = input('Введите вторую букву: ').upper()

pos1 = ord(letter1) - ord('A') + 1
pos2 = ord(letter2) - ord('A') + 1

letters = abs(pos2 - pos1) - 1

print(f'Позиции букв:\n'
      f'\t{letter1} = {pos1}\n'
      f'\t{letter2} = {pos2}\n'
      f'Между ними находится букв: {letters}.')

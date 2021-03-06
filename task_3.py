# Написать программу, которая генерирует в указанных пользователем границах: ● случайное целое число,
# ● случайное вещественное число, ● случайный символ. Для каждого из трех случаев пользователь задает свои
# границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
# https://drive.google.com/file/d/1zmsVhsIlCTU7ZL80T4OQnL8UmV2qOG4z/view?usp=sharing

from random import random

print('Введите границы диапазона генерации целого числа')
min = int(input('min = '))
max = int(input('max = '))
rnd = random()
res = int(rnd * (max - min + 1))
res = res + min
print(f'Случайное целое число = {res}')

print('Введите границы диапазона генерации вещественного числа')
min = float(input('min = '))
max = float(input('max = '))
rnd = random()
res = rnd * (max - min) + min
print(f'Случайное вещественное число = {res:0.2f}')

print('Введите границы диапазона генерации символа')
min = ord(input('min = '))
max = ord(input('max = '))
rnd = random()
res = int(rnd * (max - min + 1))
res = res + min
res = chr(res)
print(f'Случайный символ = {res}')

# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’]
# и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

str_a = input('Enter 1 hex: ')
str_b = input('Enter 2 hex: ')

a = deque(str_a.upper())
b = deque(str_b.upper())
res_plus = deque()
hex_dict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, '0': 0}
base = 16
over = 0

while a or b or over:
    num_a = a.pop() if a else '0'
    num_b = b.pop() if b else '0'
    num_res = (hex_dict[num_a] + hex_dict[num_b] + over) % base
    over = (hex_dict[num_a] + hex_dict[num_b] + over) // base
    k = [k for k, v in hex_dict.items() if v == num_res]
    res_plus.appendleft(k[0])

print(*res_plus)

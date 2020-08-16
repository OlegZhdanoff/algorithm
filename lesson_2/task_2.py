# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3
# четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

even = 0
odd = 0
num = int(input('Введите натуральное число: '))

while num:
    n = num % 10
    if n % 2:
        odd += 1
    else:
        even += 1
    num //= 10

print(f'{even=}\n{odd=}')

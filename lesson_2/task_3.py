# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если
# введено число 3486, надо вывести 6843.

def reverse(num):
    if num // 10:
        tmp = num
        exp = 0
        while tmp > 9:
            tmp //= 10
            exp += 1
        return (num % 10) * (10 ** exp) + reverse(num // 10)
    return num


num = int(input('Введите целое число'))
print(reverse(num))

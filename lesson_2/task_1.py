# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции
# вводятся пользователем. После выполнения вычисления программа не завершается, а запрашивает новые данные для
# вычислений.Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь
# вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова запрашивать знак
# операции.Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

while True:
    a = float(input('a = '))
    b = float(input('b = '))
    oper = input('Тип операции (+, -, *, /, 0): ')
    if oper == '+':
        res = a + b
    elif oper == '-':
        res = a - b
    elif oper == '*':
        res = a * b
    elif oper == '/':
        if not b:
            print('На ноль делить нельзя!')
            continue
        res = a / b
    elif oper == '0':
        break
    else:
        print('Недопустимый символ операции')
        continue
    print(f'Результат a {oper} b = {res}')

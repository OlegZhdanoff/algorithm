# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

START = 2
END = 99
res = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(START, END+1):
    for num in range(2, 10):
        if i % num == 0:
            res[num - 2] += 1

for i, el in enumerate(res):
    print(f'{i+2} = {el}')


# тот же результат можно получить простым целочисленным делением
for num in range(2, 10):
    res[num - 2] = END // num
# для компактности результат вывел в строку
print(*res)

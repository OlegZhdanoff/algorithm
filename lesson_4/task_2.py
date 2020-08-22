# 2). Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна
# принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность
# алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — без использования «Решета Эратосфена».

import timeit
import cProfile

def sieve(idx: int):
    step = 1000     # при ненахождении искомого числа, увеличиваем массив натуральных чисел на заданный шаг
    step_cnt = 0    # сколько раз мы увеличивали массив
    n = step        # текущий размер массива
    pos = 0         # текущее количество простых чисел
    a = [0] * step  # создание массива с n количеством элементов
    for i in range(n):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    erat = []
    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    try:
        while m < n:  # перебор всех элементов до заданного числа
            if a[m] != 0:  # если он не равен нулю, то
                j = m * 2  # увеличить в два раза (текущий элемент - простое число)
                if (m // step) == step_cnt:
                    pos += 1
                if pos == idx:
                    return a[m]
                while j < n:
                    a[j] = 0  # заменить на 0
                    j = j + m  # перейти в позицию на m больше
            m += 1
            if m == n and pos < idx:
                a.extend([i for i in range(n, step+n)])
                n += step
                step_cnt += 1
                # print(a[-1])
                m = 2
    except IndexError as e:
        print(f'{m=}\t{n=}\t{a[-1]=}\t{pos}')


def prime(idx: int):
    lst = [0, 2]
    if idx < 2:
        return lst[idx]
    step = 1000
    n = step
    pos = 1
    i = 3
    while i < n + 1:
        if (i > 10) and (i % 10 == 5):
            i += 2
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                pos += 1
                break
            if j and i % j == 0:
                break
        else:
            lst.append(i)
            pos += 1
        if pos == idx:
            return lst[-1]
        i += 2
        if i >= n + 1 and pos < idx:
            n += step


print(sieve(500))
print(prime(500))

# print(timeit.timeit('sieve(500)', globals=globals(), number=1000))  # 3.5184438780000002
# print(timeit.timeit('prime(500)', globals=globals(), number=1000))  # 2.16889726

# print(timeit.timeit('sieve(1000)', globals=globals(), number=1000))  # 12.876794912
# print(timeit.timeit('prime(1000)', globals=globals(), number=1000))  # 5.692605581999999

cProfile.run('sieve(50000)')
# 1   79.428   79.428   79.491   79.491 task_2.py:10(sieve)

cProfile.run('prime(50000)')
# 1    1.252    1.252    1.256    1.256 task_2.py:47(prime)

# Алгоритм без решета Эратосфена работает намного эффективнее и быстрее, т.к. не надо проходить подряд по всем
# натуральным числам

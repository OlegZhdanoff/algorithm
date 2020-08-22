# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
# трех уроков.
# Для анализа было взято задание 3.1 - Определить, какое число в массиве встречается чаще всего.

import random
import timeit
import cProfile
import functools

SIZE = 1_000
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(array)


# первый вариант
def max_cnt_double_cycle(array):
    max_ = 0
    max_idx = 0
    for i, num in enumerate(array):
        cur = 0
        for el in array:
            if num == el:
                cur += 1
        if cur > max_:
            max_ = cur
            max_idx = i
    # print(array[max_idx])


# второй вариант
def max_cnt_cycle(array):
    num_dict = dict()
    max_cnt = 0
    max_ = None
    for num in array:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
        if num_dict[num] > max_cnt:
            max_cnt = num_dict[num]
            max_ = num
    # print(max_, max_cnt)


# третий вариант
def max_cnt(array):
    num_dict = dict()
    for num in array:
        if num not in num_dict:
            num_dict[num] = array.count(num)
    final_dict = dict([max(num_dict.items(), key=lambda k_v: k_v[1])])
    # print(final_dict)


print(timeit.timeit('max_cnt_double_cycle(array)', globals=globals(), number=100))
# 0.042807152   -- > SIZE = 100 MAX_ITEM = 10
# 3.69860931   -- > SIZE = 1_000 MAX_ITEM = 10
# 345.360979906 -- > SIZE = 10_000 MAX_ITEM = 10

print(timeit.timeit('max_cnt_cycle(array)', globals=globals(), number=1000))
# 0.184185388   -- > SIZE = 1_000 MAX_ITEM = 10
# 0.179933717   -- > SIZE = 1_000 MAX_ITEM = 100
# 1.922109166 -- > SIZE = 10_000 MAX_ITEM = 10
# 19.30097967 -- > SIZE = 100_000 MAX_ITEM = 10

print(timeit.timeit('max_cnt(array)', globals=globals(), number=1000))
# 0.25346568999999997   -- > SIZE = 1_000 MAX_ITEM = 10
# 1.662260649   -- > SIZE = 1_000 MAX_ITEM = 100
# 2.0468984349999997 -- > SIZE = 10_000 MAX_ITEM = 10
# 21.641872013 -- > SIZE = 100_000 MAX_ITEM = 10

cProfile.run('max_cnt_double_cycle(array)')
# 1   89.548   89.548   89.548   89.548 task_1.py:16(max_cnt_double_cycle)   -- > SIZE = 50_000 MAX_ITEM = 10
cProfile.run('max_cnt_cycle(array)')
# 1    0.009    0.009    0.009    0.009 task_1.py:31(max_cnt_cycle)  -- > SIZE = 50_000 MAX_ITEM = 10
# 1    1.818    1.818    1.818    1.818 task_1.py:31(max_cnt_cycle)  -- > SIZE = 10_000_000 MAX_ITEM = 10
# 1    0.245    0.245    0.245    0.245 task_1.py:31(max_cnt_cycle)  -- >  -- > SIZE = 1_000_000 MAX_ITEM = 1000
cProfile.run('max_cnt(array)')
# 1    0.002    0.002    0.010    0.010 task_1.py:47(max_cnt) -- > -- > SIZE = 50_000 MAX_ITEM = 10
# 1    0.340    0.340    2.024    2.024 task_1.py:47(max_cnt) -- > SIZE = 10_000_000 MAX_ITEM = 10
# 1    0.056    0.056   16.254   16.254 task_1.py:47(max_cnt) -- > SIZE = 1_000_000 MAX_ITEM = 1000

# Первый вариант max_cnt_double_cycle очень медленный из-за вложенного цикла и имеет квадратичную сложность О(n**2)
# Второй вариант max_cnt_cycle самый оптимальный, т.к. за один проход массива решает поставленную задачу.
# Третий вариант max_cnt использует встроенные функции и сильно зависит от количества разных цифр (MAX_ITEM) в массиве,
# при низких значениях MAX_ITEM (например 10) скорость совсем немного ниже чем у второго варианта, хотя в третьем
# используется встроенная функция count, которая перебирает все элементы массива, но за счет того, что встроенные
# функции написаны на С и скомпилированы, они выполняются довольно таки быстро.

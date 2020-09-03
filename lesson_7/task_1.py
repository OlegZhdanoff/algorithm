# 1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

import random
import cProfile

SIZE = 10000
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# array = [9, 5, 3, 8, 0, 1, 2, 6, 7, 4]


def bubble_classic(arr):
    n = 1
    while n < len(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n += 1


def bubble_fast(arr):
    n = 1
    while n < len(arr):
        is_changed = False
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_changed = True
        if not is_changed:
            break
        n += 1
        # print(array)


cProfile.run('bubble_classic(array)')
# 1   14.701   14.701   14.704   14.704 task_1.py:16(bubble_classic)
random.shuffle(array)
cProfile.run('bubble_fast(array)')
# 1    9.548    9.548    9.550    9.550 task_1.py:25(bubble_fast)
print(array)

# Из теста видно, что оптимизация дала свои результаты. Во внутреннем цикле перебираем массив не до конца, а только
# несортированную часть массива, а также используем флаг для проверки массива на отсортированность.

# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_, max_ = 0, 0

for i, el in enumerate(array):
    if array[min_] > el:
        min_ = i
    if array[max_] < el:
        max_ = i

array[min_], array[max_] = array[max_], array[min_]
print(array)

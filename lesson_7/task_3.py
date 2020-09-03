# 3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.

import random

size = int(input('Enter m: '))
size = 2 * size + 1
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
print(array)


def quickselect(l, k, pivot_fn=random.choice):
    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


print(f'Median = {quickselect(array, len(array) / 2)}')

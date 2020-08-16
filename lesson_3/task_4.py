# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 15
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

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

print(array[max_idx])

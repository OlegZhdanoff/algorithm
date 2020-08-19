# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно
# разных значения.

import random

SIZE = 15
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_ = array[0]
max_idx = 0

for i, el in enumerate(array):
    if el < 0:
        if max_ < el:
            max_ = el
            max_idx = i

print(f'Max negative number: array[{max_idx}] = {array[max_idx]}')

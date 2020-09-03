# 1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 100
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# array = [9, 5, 3, 8, 0, 1, 2, 6, 7, 4]

n = 1
while n < len(array):
    is_changed = False
    for i in range(len(array) - n):
        if array[i] < array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            is_changed = True
    if not is_changed:
        break
    n += 1
    # print(array)

print(array)

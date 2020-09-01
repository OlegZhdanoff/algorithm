# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Для анализа было взято задание 3.1 - Определить, какое число в массиве встречается чаще всего.

import random
import sys

SIZE = 10000
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(array)


def calc_size(x):
    res = 0
    # print(f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                res += calc_size(key)
                res += calc_size(value)
        elif not isinstance(x, str):
            for item in x:
                res += calc_size(item)
                # print(f'type={type(item)}, size={sys.getsizeof(item)}, obj={item}, {res=}')
    res += sys.getsizeof(x)
    return res


def get_size(var_dict):
    res = 0
    for name, var in var_dict.items():
        res += calc_size(var)
        # print(name, var)
    return res


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
    print(f'Function max_cnt_double_cycle used: {get_size(locals())} bytes')


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
    print(f'Function max_cnt_cycle used: {get_size(locals())} bytes')


# третий вариант
def max_cnt(array):
    num_dict = dict()
    for num in array:
        if num not in num_dict:
            num_dict[num] = array.count(num)
    final_dict = dict([max(num_dict.items(), key=lambda k_v: k_v[1])])
    print(f'Function max_cnt used: {get_size(locals())} bytes')


max_cnt_double_cycle(array)
max_cnt_cycle(array)
max_cnt(array)

# Первая функция использует меньше всего памяти, т.к. для своей работы используют только простые переменные типа int.
# Вторая функция исплользует для своей работы дополнительный словарь, который съедает дополнительную память,
# в зависимости от количества уникальных цифр в исходном массиве
# В третьем варианте для нахождения результат исплользуем еще один словарь из одного элемента, что добавляет 232 байта
# При большом объеме исходного массива разница в процентном соотношении используемой памяти становится незначительной,
# поэтому первую функцию, использующую самый маленький объем памяти, все равно не выгодно испльзовать, т.к. выигрыш
# в памяти совершенно не соизмерим со скоростью работы, по сравнению с другими вариантами
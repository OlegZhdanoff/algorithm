# 1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9
#

import hashlib


def sub_str_cnt(s: str):
    sub_str_set = set()

    def str_count(st: str, length: int, str_set: set):

        if length > 1:
            str_count(st, length - 1, str_set)
        for i in range(len(s) - length + 1):
            s_hash = hashlib.sha1(st[i:i + length].encode('utf-8')).hexdigest()
            str_set.add(s_hash)

    str_count(s, len(s) - 1, sub_str_set)
    return len(sub_str_set)


print(sub_str_cnt('sova'))

# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для
# каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict

corp_cnt = int(input('Enter number of corporations: '))
corp_dict = defaultdict(int)
for i in range(corp_cnt):
    name = input(f'Enter name of {i+1} corporation: ')
    for k in range(4):
        profit = int(input(f'Enter profit per {k+1} quarter for {name}: '))
        corp_dict[name] += profit

avg = int(sum(corp_dict.values()) / len(corp_dict.values()))

losers = []
print(f'Profit greater than average: ')
for corp in corp_dict:
    print(f'{corp}', end='\t') if corp_dict[corp] >= avg else losers.append(corp)

print('\nProfit lesser than average:\n', *losers, sep='\t')

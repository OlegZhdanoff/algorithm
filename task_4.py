# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
# https://drive.google.com/file/d/1zmsVhsIlCTU7ZL80T4OQnL8UmV2qOG4z/view?usp=sharing

first = ord(input('Введите первую букву: '))
second = ord(input('Введите вторую букву: '))
first = first - ord('a') + 1
second = second - ord('a') + 1
print(f'Позиции введеных букв: {first=} и {second=}')
num = abs(first-second)-1
print('Количество символов между заданными буквами:', num)

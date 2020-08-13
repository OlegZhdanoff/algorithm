# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# https://drive.google.com/file/d/1zmsVhsIlCTU7ZL80T4OQnL8UmV2qOG4z/view?usp=sharing

num = int(input('Введите номер буквы в алфавите: '))
num = ord('a') + num - 1
char = chr(num)
print('Вы ввели букву:', char)

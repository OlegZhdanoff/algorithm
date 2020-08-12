# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

num = int(input("Введите трехзначное число: "))

ones = num % 10
dozens = num % 100 // 10
hundreds = num // 100

sum = ones + dozens + hundreds
mult = ones * dozens * hundreds

print("Сумма цифр числа:", sum)
print("Произведение цифр числа:", mult)

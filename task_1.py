

num = int(input("Введите трехзначное число: "))

ones = n % 10
dozens = n % 100 // 10
hundreds = n // 100

sum = ones + dozens + hundreds
mult = ones * dozens * hundreds

print("Сумма цифр числа:", sum)
print("Произведение цифр числа:", mult)
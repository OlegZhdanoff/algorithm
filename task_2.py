# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти
# точки
# https://drive.google.com/file/d/1zmsVhsIlCTU7ZL80T4OQnL8UmV2qOG4z/view?usp=sharing

print("Введите координаты первой точки:")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))

print("Введите координаты второй точки")
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

print("Уравнение прямой, проходящей через эти точки:")
print(f"y = {k:0.2f} * x + {b:0.2f}")

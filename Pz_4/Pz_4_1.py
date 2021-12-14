# Дано целое число N (>0)
# Найти произведение 1.1 * 1.2 * 1.3 * ... (N сомножителей)

n = input("Введите число: ")
while type(n) != int: # Проверка исключений.
    try:
        n = int(n)
    except ValueError:
        print("Введеноневерноечисло.")
        n = input("Введите число: ")

try:
    while n < 0:     # n - положительное число.
        print("Введено неверное число.")
        n = input("Введите число: ")
except TypeError:
    pass

f = 1.1
m = 0.1
k = 1
p = 1

while k <= n:
    p *= f
    f += m
    k += 1
print(round(p, 2))

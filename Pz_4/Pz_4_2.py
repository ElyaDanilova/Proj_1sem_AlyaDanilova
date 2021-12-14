# Дано целое число N (>1)
# Найти наименьшее целое K, при котором выполянетсянерванество 3**K > N

n = input("Введите число: ")
while type(n) != int: # Проверка исключений.
    try:
        n = int(n)
    except ValueError:
        print("Введеноневерноечисло.")
        n = input("Введите число: ")
try:
    while n < 1:
        print("Введено неверное число.")
        n = input("Введитечисло: ")
except TypeError:
    pass

k = 0
p = 0

while p < n:
    p = 3**k
    if p <= n:
        k += 1

print(k)

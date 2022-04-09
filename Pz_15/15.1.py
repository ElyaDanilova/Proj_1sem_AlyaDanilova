# В матрице найти сумму и произведение элементов
# строки N (N задать с клавиатуры).

import random

k = int(input('Введите количество столбцов: '))
m = int(input('Введите количество строк: '))
n = int(input('Введите номер строки: '))
while n > m:
    try:
        print('Введен неверный номер строки.')
        n = int(input('Введите номер строки: '))
    except ValueError:
        pass
s = 0
p = 1
matr = [[random.randint(1, 10) for x in range(k)]for y in range(m)]
print()
print('Исходная матрица:')
for v in matr:
    print(v)
print()
for j in range(k):
    s += matr[n-1][j]
    p *= matr[n-1][j]
print('Сумма и произведение элементов выбранной строки:', '\n', s, p)
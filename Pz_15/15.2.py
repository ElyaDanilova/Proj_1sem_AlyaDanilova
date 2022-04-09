# В матрице найти сумму элементов второй половины матрицы.

import random

k = int(input('Введите количество столбцов: '))
while k % 2 != 0:
    try:
        print('Количество столбцов должно быть четным.')
        k = int(input('Введите количество столбцов: '))
    except ValueError:
        pass
m = int(input('Введите количество строк: '))
s = 0
matr = [[random.randint(1, 10) for x in range(k)]for y in range(m)]
print()
print('Исходная матрица:')
for v in matr:
    print(v)
print()
h = int(k / 2)
for j in range(m):
    for i in range(h):
        s += matr[j][i-h]

print('Сумма элементов второй половины матрицы:', '\n', s)
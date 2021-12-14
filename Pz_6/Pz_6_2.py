# Дано число Rи список А размера N. Найти элемент списка, который
# наиболее близок к числу R ( то есть такой элемент Ак, для которого
# величина |Aк - R| является максимальной).

from random import randint

r = int(input("Введите r: "))
n = int(input("Введите размер списка: "))
a = [randint(0, 10) for i in range(n)]
c = []
print("Исходный список: ", a)

for i in range(n):
    c.append(abs(a[i] - r))

print(c)
print("Ближайший к r элемент: ", abs(min(c)-r))

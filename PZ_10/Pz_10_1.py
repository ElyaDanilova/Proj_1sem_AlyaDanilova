#Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Минимальный элемент:
#Количество положительных элементов в первой половине:


import random

n = 0
a = []

f1 = open("file1.txt", "w", encoding="UTF-8")
for i in range(random.randint(10, 20)):
    a.append(random.randint(-10, -10))
    f1.write(str(a[i]))
    f1.write(" ")
f1.close() #Мы создали список из положительных "рандомных" цифр и заполнили ими файл

f1 = open("file1.txt")
l = f1.read()
f1.close()

f2 = open("file1.txt", "w", encoding="UTF-8") #Построчно заполнен файл по заданию
f2.write(l)
f2.write("Исходные данные: \n")
f2.write(l)
f2.write("Количество элементов: \n")
f2.write("\n")
f2.write(str(len(a)))
f2.write("Минимальный элемент: \n")
f2.write(str(min(a)))
f2.write("\n")
f2.write("Количество положительных элементов в первой половине: \n")
for i in range(int(len(a)/2)):
     if a[i] > 0:
         n += 1
f2.write(str(n))


# Из исходного текстового файла (Dostoevsky.txt) выбрать
# блок информации за 1857 год и поместить ее в новый
# текстовый файл.

import re

p = re.compile(r"[1][8][5][7][ а-яА-Я,\-–.\n]+[.]")
with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()
print("Выбранный блок:")
print(p.findall(text))

x = str(p.findall(text))
z = x.split('\\n')
f1 = open('new.txt', 'w', encoding='utf-8')
for i in z:
    f1.write(i)
    f1.write('\n')
f1.close()
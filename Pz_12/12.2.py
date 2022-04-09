import tkinter
from tkinter import *
from tkinter import ttk


def Chet(event):
    t = 0

    n1 = int(num1.get())
    n2 = int(num2.get())

    t = t + 1 if ((n1 % 2 == 0) and (n2 % 2 == 0)) or\
                 ((n1 % 2 != 0) and (n2 % 2 != 0))else t

    if t == 1:
        positive['text'] = "Высказывание «Числа A и B имеют" \
                           " одинаковую четность» - истина."
    else:
        negative['text'] = "Высказывание «Числа A и B имеют" \
                           " одинаковую четность» - ложь."


root = Tk()
root.title('Четность')
root.geometry('500x200')

label1 = Label(root, text="Введите число A: ", font='Arial 12')
label1.place(x=25, y=20)
num1 = Entry()
num1.place(x=275, y=25)

label2 = Label(root, text="Введите число B: ", font='Arial 12')
label2.place(x=25, y=45)
num2 = Entry()
num2.place(x=275, y=50)

button1 = Button(text="Обработать")
button1.place(x=200, y=115)

positive = Label()
positive.place(x=50, y=150)

negative = Label()
negative.place(x=50, y=150)

button1.bind('<Button-1>', Chet)

root.mainloop()

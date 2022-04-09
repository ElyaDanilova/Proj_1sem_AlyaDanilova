from tkinter import *
root = Tk()
root.geometry('430x590')
root.config(bg='darkgray')

label1 = Label(root, text='Contact Us', width=23, height=1, font='arial 25',
               bg='dimgrey', fg='black')
label1.place(x=0, y=35)

label2 = Label(root, text='First Name', width=10, height=1, bg='darkgray',
               font='arial 14')
label2.place(x=25, y=115)
entry1 = Entry(width=35)
entry1.place(x=40, y=140)

label3 = Label(root, text='Last Name', width=10, height=1, bg='darkgray',
               font='arial 14')
label3.place(x=25, y=175)
entry2 = Entry(width=35)
entry2.place(x=40, y=200)

label4 = Label(root, text='Email', width=6, height=1, bg='darkgray',
               font='arial 14')
label4.place(x=25, y=235)
entry3 = Entry(width=35)
entry3.place(x=40, y=260)

label5 = Label(root, text='Website', width=8, height=1, bg='darkgray',
               font='arial 14')
label5.place(x=25, y=295)
entry4 = Entry(width=35)
entry4.place(x=40, y=320)

label6 = Label(root, text='Password', width=9, height=1, bg='darkgray',
               font='arial 14')
label6.place(x=25, y=355)
entry5 = Entry(width=35)
entry5.place(x=40, y=380)

label7 = Label(root, text='Password Confirmation', width=19, height=1,
               bg='darkgray', font='arial 14')
label7.place(x=25, y=415)
entry6 = Entry(width=35)
entry6.place(x=40, y=440)

button1 = Button(root, text='sign on', width=5, height=1, font='arial 10    ')
button1.place(x=40, y=475)
root.mainloop()
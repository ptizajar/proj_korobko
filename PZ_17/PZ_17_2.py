# Вариант 13. Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ №№ 2 – 9.
# ПЗ№3.Даны три целых числа: A, B, C. Проверить истинность высказывания:"Хотя бы одно из чисел A, B, C положительное"
from tkinter import *
from tkinter import messagebox

def sravn():
    try:
       a = int(entry1.get())
       b = int(entry2.get())
       c = int(entry3.get())
       if a > 0 or b > 0 or c > 0:
          messagebox.showinfo(message="""Высказывание: "Хотя бы одно из чисел A, B, C положительное" истинно""")
       else:
          messagebox.showinfo(message="""Высказывание: "Хотя бы одно из чисел A, B, C положительное" ложно""")
    except:
       messagebox.showinfo(message='Вы ввели что-то не то')

root = Tk()
root.geometry('170x200')
label1 = Label(text="Целое число А:")
entry1 = Entry()
label2 = Label(text="Целое число B:")
entry2 = Entry()
label3 = Label(text="Целое число C:")
entry3 = Entry()
button1 = Button(text='Проверить',command=sravn)
label1.place(x=20, y=10)
entry1.place(x=20, y=30)
label2.place(x=20, y=50)
entry2.place(x=20, y=70)
label3.place(x=20, y=90)
entry3.place(x=20, y=110)
button1.place(x=20, y=150)

root.mainloop()
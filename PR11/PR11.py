import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


def calkulating():
    perem1 = ent1.get()
    perem2 = ent2.get()
    deistv = combo.get()
    if deistv == '+':
        otvet = int(perem1) + int(perem2)
        ent3.delete(0, tk.END)
        ent3.insert(0, otvet)
    elif deistv == '-':
        otvet = int(perem1) - int(perem2)
        ent3.delete(0, tk.END)
        ent3.insert(0, otvet)
    elif deistv == '*':
        otvet = int(perem1) * int(perem2)
        ent3.delete(0, tk.END)
        ent3.insert(0, otvet)
    else:
        otvet = int(perem1) / int(perem2)
        ent3.delete(0, tk.END)
        ent3.insert(0, otvet)


def chekker():
    message = ''
    if ch1.get() == 1:
        message += 'первый вариант; '
    if ch2.get() == 1:
        message += 'второй вариант; '
    if ch3.get() == 1:
        message += 'третий вариант; '
    messagebox.showinfo('Вы выбрали', message)


def failiki():
    puti = filedialog.askopenfilename()
    file = open(puti, 'r', encoding='utf-8')
    text.insert(tk.END, file.read())


win = tk.Tk()
win.title('11 Практика. Дементеев Дмитрий Николаевич')
win.geometry('900x600+500+100')
win.config(bg='#b4e0d7')


note = ttk.Notebook(win)
note.pack(pady=10, padx=10)


vcl1 = ttk.Frame(note)
vcl2 = ttk.Frame(note)
vcl3 = ttk.Frame(note)

note.add(vcl1, text='Калькулятор')
note.add(vcl2, text='Выбор чекбокса')
note.add(vcl3, text='Текст')

ent1 = tk.Entry(vcl1, width=10)
ent1.grid(row=0, column=0)

combo = ttk.Combobox(vcl1, width=3)
combo['values'] = ('+', '-', '*', '/')
combo.current(0)  # установите вариант по умолчанию
combo.grid(row=0, column=1, padx=5)

ent2 = tk.Entry(vcl1, width=10)
ent2.grid(row=0, column=2, padx=5)

btn1 = tk.Button(vcl1, text='=', command=calkulating)
btn1.grid(row=0, column=3, padx=5)

ent3 = tk.Entry(vcl1, width=10)
ent3.grid(row=0, column=4, padx=5)

lab2 = tk.Label(vcl1, text='-- Калькулятор', font=1)
lab2.grid(row=0, column=5)

ch1 = tk.IntVar()
ch2 = tk.IntVar()
ch3 = tk.IntVar()

chek1 = tk.Checkbutton(vcl2, text='Первый', variable=ch1)
chek2 = tk.Checkbutton(vcl2, text='Второй', variable=ch2)
chek3 = tk.Checkbutton(vcl2, text='Третий', variable=ch3)

chek1.grid(row=1, column=0)
chek2.grid(row=2, column=0)
chek3.grid(row=3, column=0)

btn2 = tk.Button(vcl2, text='Подтвердить выбор', command=chekker)
btn2.grid(row=2, column=1)

menu = tk.Menu(win)
win.config(menu=menu)

file = tk.Menu(menu)
menu.add_cascade(label='Открыть текстовый файл', menu=file)
file.add_command(label='Выбор нужного файла', command=failiki)

text = tk.Text(vcl3, wrap='word')
text.pack(fill='both', expand=True)

win.mainloop()

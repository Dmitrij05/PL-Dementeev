## openshift/origin - имя репозитория
import tkinter as tk
import requests
import json


def json_function():
    name = ent.get()
    link = f'https://api.github.com/repos/{name}'
    inf = requests.get(link)
    findings = inf.json()

    vivod = {
        'company': findings.get('company', 'None'),
        'created_at': findings.get('created_at', 'None'),
        'email': findings.get('email', 'None'),
        'id': findings.get('id', 'None'),
        'name': findings.get('name', 'None'),
        'url': findings.get('url', 'None')
    }

    file = open('Dementeev_Json.json', 'w')
    json.dump(vivod, file, indent=1)


win = tk.Tk()
win.title('12 Практика. Дементеев Дмитрий Николаевич')
win.geometry('500x100+500+300')
win.config(bg='#b4e0d7')

lab = tk.Label(win, text='Имя репозитория:', bg='#b4e0d7')
lab.grid(row=0, column=0, padx=10)

ent = tk.Entry(win)
ent.grid(row=1, column=1, padx=10)

btn = tk.Button(win, text='Загрузить информацию', command=json_function)
btn.grid(row=2, column=2, padx=10)

win.mainloop()

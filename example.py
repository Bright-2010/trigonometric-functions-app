import requests
import tkinter as tk
from tkinter import ttk
def re_num():
    http=requests.get(
        "https://api.brightweb.top/trig",
        params={
            "type": var.get(),
            "deg": enter_var.get()
        }
    )
    print(http.json())
    answer_lable.config(text="结果是:"+str(http.json()['result']))

win=tk.Tk()
win.title("三角函数计算器")
win.geometry("400x500")
tk.Label(text="三角函数计算器",font=(None,18)).pack()

var=tk.StringVar()
choose=ttk.Combobox(values=["sin","cos","tan"],state="readonly",textvariable=var)
choose.current(0)
choose.pack()

enter_var=tk.StringVar()
enterbox=tk.Entry(win,textvariable=enter_var)
enterbox.pack()

OK_button=tk.Button(text="计算",font=(None,16),command=re_num)
OK_button.pack()

answer_lable=tk.Label(text="结果是:",font=(None,16))
answer_lable.pack()
win.mainloop()
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 09:04:09 2020

"""

import tkinter as tk
import tkinter.messagebox
def clickme():
    tkinter.messagebox.showinfo(title='訊息',message='按鈕已被點選')
    var.set('按鈕被點選了') #設定var的值為按鈕被點選了
    
def cancelme():
    var.set('') #設定var的值為按鈕被點選了
    
window = tk.Tk()
window.title('my first GUI')
window.geometry('300x300')

var = tk.StringVar()    # 用var來接收clickme函式的傳出內容用以顯示在entry上


label = tk.Label(window, text='GUI',bg='#f68',fg='#bf5',width='20')
label.pack()

entry = tk.Entry(window,text=var,width='20')
entry.pack()

button = tk.Button(window,text='點選',command = clickme)
button.pack()

cbutton = tk.Button(window,text='清空',command = cancelme)
cbutton.pack()

window.mainloop()
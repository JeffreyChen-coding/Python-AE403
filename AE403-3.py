# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 09:04:09 2020

"""

import tkinter as tk
import tkinter.messagebox

def clickme():
    tkinter.messagebox.showinfo(title='訊息',message='按鈕已被點選')
   
    
window = tk.Tk()
window.title('my first GUI')
window.geometry('300x300')

var = tk.StringVar()    # 將label標籤的內容設定為字元型別，用var來接收hit_me函式的傳出內容用以顯示在標籤上

label = tk.Label(window, text='GUI')
label.pack()
entry = tk.Entry(window,width='20')
entry.pack()
button = tk.Button(window,text='按鈕',command = clickme)
button.pack()
window.mainloop()

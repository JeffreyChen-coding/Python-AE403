# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 09:04:09 2020

"""

import tkinter as tk  
window = tk.Tk()
window.title('my first GUI')
window.geometry('300x300')
label = tk.Label(window, text='GUI',bg='#f68',fg='#bf5',width='20')
label.pack()
entry = tk.Entry(window,width='20')
entry.pack()
button = tk.Button(window,text='按鈕')
button.pack()
window.mainloop()
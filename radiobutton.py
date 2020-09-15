# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 13:00:49 2020

@author: K0718
"""

import tkinter as tk
window = tk.Tk()
window.title("單選按鈕")
window.geometry('500x500')

string = tk.StringVar()
gender=tk.StringVar()

def selection():
    label.config(text="我是"+gender.get()+",我喜歡" + string.get())
label = tk.Label(window,bg='#f00',text='尚未選擇')
label.pack()

radio1=tk.Radiobutton(window,text='Minecraft Python',variable=string,value='Minecraft Python',command=selection)
radio1.pack()

radio2=tk.Radiobutton(window,text='Pygame',variable=string,value='Pygame',command=selection)
radio2.pack()

radio3=tk.Radiobutton(window,text='Tkinter',variable=string,value='Tkinter',command=selection)
radio3.pack()

string.set("Tkinter")
selection()

radio4=tk.Radiobutton(window,text='男生',variable=gender,value='男生',command=selection)
radio4.pack()

radio5=tk.Radiobutton(window,text='女生',variable=gender,value='女生',command=selection)
radio5.pack()




gender.set("男生")
selection()


window.mainloop()
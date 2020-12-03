# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 08:32:50 2020


"""

import tkinter as tk
window=tk.Tk()
window.geometry("500x500")
window.title("四則運算")


#預設符號為+
var=tk.StringVar()
var.set("+")

num1=tk.StringVar()
num2=tk.StringVar()

total=tk.StringVar()

def cal():
       exp = num1.get()+var.get()+num2.get()
       result=str(eval(exp))#將運算式進行計算
       total.set(result)
     



tk.Label(window,text="數字1:").grid(row=3,column=1,padx=5,pady=5)
tk.Entry(window,width=10,textvariable=num1).grid(row=3,column=2,padx=5,pady=5)

tk.Radiobutton(window,text="+",variable=var,value="+").grid(row=2,column=4,padx=5,pady=5)
tk.Radiobutton(window,text="-",variable=var,value="-").grid(row=3,column=4,padx=5,pady=5)
tk.Radiobutton(window,text="*",variable=var,value="*").grid(row=4,column=4,padx=5,pady=5)
tk.Radiobutton(window,text="/",variable=var,value="/").grid(row=5,column=4,padx=5,pady=5)

tk.Label(window,text="數字2:").grid(row=3,column=5,padx=5,pady=5)
tk.Entry(window,width=10,textvariable=num2).grid(row=3,column=6,padx=5,pady=5)

tk.Button(window,text="=",command=cal).grid(row=3,column=7)

tk.Entry(window,width=10,textvariable=total).grid(row=3,column=8,padx=5,pady=5)
window.mainloop()
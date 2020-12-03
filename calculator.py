# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 09:23:45 2020


"""


import tkinter as tk
window=tk.Tk()
window.geometry("300x300")
window.resizable(False, False)
window.title("計算機")


#預設符號為+
var=tk.StringVar()
var.set("+")

num1=tk.StringVar()
num2=tk.StringVar()

total=tk.StringVar()
result=''
shownum=''
def cal(val):
       global result
       global shownum
       
       if val!='C' and val!='=' and val!='+' and val!='-' and val!='*' and val!='/':
           shownum+=str(val)
       else:
           shownum=''
       
       if val!='C' and val!='=':
           result+=str(val) #取得運算式

        
       if val == 'C':#使用者點選'C'時，清空運算式，並顯示0
           result=''
           total.set(0)
           
       elif val == '=':      
           fresult=str(eval(result))
           total.set(fresult)
           result=fresult#將運算式設為現在的值
           
       else:
           total.set(str(shownum))
           
total=tk.StringVar()   

label=tk.Entry(window,state="readonly",textvariable=total,width=10).grid(row=0,column=1)

tk.Button(window,text="1",width=10,height=2,command=lambda:cal('1')).grid(row=1,column=1)
tk.Button(window,text="2",width=10,height=2,command=lambda:cal('2')).grid(row=1,column=2)
tk.Button(window,text="3",width=10,height=2,command=lambda:cal('3')).grid(row=1,column=3)
tk.Button(window,text="4",width=10,height=2,command=lambda:cal('4')).grid(row=2,column=1)
tk.Button(window,text="5",width=10,height=2,command=lambda:cal('5')).grid(row=2,column=2)
tk.Button(window,text="6",width=10,height=2,command=lambda:cal('6')).grid(row=2,column=3)
tk.Button(window,text="7",width=10,height=2,command=lambda:cal('7')).grid(row=3,column=1)
tk.Button(window,text="8",width=10,height=2,command=lambda:cal('8')).grid(row=3,column=2)
tk.Button(window,text="9",width=10,height=2,command=lambda:cal('9')).grid(row=3,column=3)
tk.Button(window,text="0",width=10,height=2,command=lambda:cal('0')).grid(row=4,column=1)
tk.Button(window,text=".",width=10,height=2,command=lambda:cal('.')).grid(row=4,column=2)
tk.Button(window,text="+",width=10,height=2,command=lambda:cal('+')).grid(row=4,column=3)
tk.Button(window,text="-",width=10,height=2,command=lambda:cal('-')).grid(row=5,column=1)
tk.Button(window,text="x",width=10,height=2,command=lambda:cal('*')).grid(row=5,column=2)
tk.Button(window,text="/",width=10,height=2,command=lambda:cal('/')).grid(row=5,column=3)
tk.Button(window,text="C",width=10,height=2,command=lambda:cal('C')).grid(row=6,column=1)
tk.Button(window,text="=",width=10,height=2,command=lambda:cal('=')).grid(row=6,column=2)

window.mainloop()


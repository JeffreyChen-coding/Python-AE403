# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:50:14 2020

@author: K0718
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 13:31:14 2020

@author: K0718
"""
#利用tkinter Label、button、entry、showmessage製作簡易點餐系統

import tkinter as tk
import tkinter.messagebox
window=tk.Tk()
window.title("點餐系統")
window.geometry("500x500")

#step1 定義變數
total=0 #總金額
ham=0 #漢堡金額
fre=0 #薯條金額
chi=0 #雞塊金額
co=0 #可樂金額
meal='' #餐點清單

#step2 定義函式

#漢堡函式
def hambuger():
   global total
   global ham
   total+=20
   ham+=1
   price.set(total)

#薯條函式
def fresh():
   global total
   global fre
   total+=10
   fre+=1
   price.set(total)
   

#雞塊函式
def chicken():
   global total
   global chi
   total+=25
   chi+=1
   price.set(total)

#可樂函式
def cola():
   global total
   global co
   total+=5
   co+=1
   price.set(total)
   


#重新點餐函式
def reset():
   global total
   global ham
   global fre
   global chi
   global co 
   global meal
   total=0
   ham=0
   fre=0
   chi=0
   co=0
   meal=''
   price.set(total)

#確定點餐
def accept():
    global total
    global ham
    global fre
    global chi
    global co
    global meal
    if ham > 0:
      meal= "漢堡"+" * "+str(ham)+"\n"
    if fre>0:
      meal+= "薯條"+" * "+str(fre)+"\n" 
      
    if chi>0:
      meal+= "雞塊"+" * "+str(chi)+"\n"
      
    if co>0:
      meal+= "可樂"+" * "+str(co)+"\n"
    
    if meal=='':
        tkinter.messagebox.showinfo(title='餐點',message="沒有任何餐點") 
    else:
        meal+="\n"+"共"+str(total)+"元"
        tkinter.messagebox.showinfo(title='餐點',message=meal) 
    total=0
    ham=0
    fre=0
    chi=0
    co=0
    meal=''
    price.set(total)
    
    
price=tk.StringVar()
tk.Label(window,text="金額：").grid(row=1,column=1)
tk.Entry(window,width=10,textvariable=price,state="readonly").grid(row=1,column=2)

tk.Label(window,text="",width=10).grid(row=2,column=1)#空一列

tk.Button(window,text="漢堡\n$20",width=10,height=5,command=hambuger).grid(row=3,column=1)
tk.Button(window,text="薯條\n$10",width=10,height=5,command=fresh).grid(row=3,column=2)
tk.Button(window,text="雞塊\n$25",width=10,height=5,command=chicken).grid(row=3,column=3)
tk.Button(window,text="可樂\n$5",width=10,height=5,command=cola).grid(row=3,column=4)

tk.Label(window,text="",width=10).grid(row=4,column=1)

tk.Button(window,text="結帳",width=10,height=1,command=accept).grid(row=5,column=1)
tk.Button(window,text="重新點餐",width=10,height=1,command=reset).grid(row=5,column=2)




  



window.mainloop()
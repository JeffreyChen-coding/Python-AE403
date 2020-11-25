# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:24:11 2020


"""

import tkinter as tk
import tkinter.messagebox
window=tk.Tk()
window.title("點餐系統")
window.geometry("500x500")



#宣告變數
total=0 #原始金額
ototal=0#折扣後的金額
hambugernum=0#漢堡數量
friesnum=0#薯條數量
chickennum=0#雞塊數量
colanum=0#可樂數量
mealnum=0#餐點總數量
meal=''#餐點清單
disoff=1#折扣預設為1，素示沒有折扣

#餐點金額與數量
def order(product,val):
    global total
    global ototal
    global hambugernum
    global friesnum
    global chickennum
    global colanum
    global mealnum
    global disoff
    total+=val
    ototal+=val
    if product=='hambuger':
        hambugernum+=1
    if product=='fries':
        friesnum+=1
    if product=='chicken':
        chickennum+=1
    if product=='cola':
        colanum+=1
    mealnum+=1
    price.set(ototal*disoff)

#折扣
def discount(val):
    global total
    global ototal
    global disoff
    disoff=val
    total=ototal*disoff
    price.set(total)
    
#結帳
def accept():
    global total
    global ototal
    global hambugernum
    global friesnum
    global chickennum
    global colanum
    global mealnum
    global disoff
    global meal
    
    if hambugernum>0:
        meal+="漢堡 * "+str(hambugernum)+"\n"
    if friesnum>0:
        meal+="薯條 * "+str(friesnum)+"\n"
    if chickennum>0:
        meal+="雞塊 * "+str(chickennum)+"\n"
    if colanum>0:
        meal+="可樂 * "+str(colanum)+"\n"    
    total=ototal*disoff
    if meal=='':
        tkinter.messagebox.showinfo(title='餐點',message="沒有任何餐點") 
    else:
        meal+=str(mealnum)+"份餐點"+"，"+"共"+str(total)+"元"
        tkinter.messagebox.showinfo(title='餐點',message=meal)
    total=0
    ototal=0
    hambugernum=0
    friesnum=0
    chickennum=0
    colanum=0
    mealnum=0
    disoff=1
    meal=''
    price.set(total)
    disc.set(1)
    
#重新點餐
def reset():
    global total
    global ototal
    global hambugernum
    global friesnum
    global chickennum
    global colanum
    global mealnum
    global disoff
    global meal
    
    total=0
    ototal=0
    hambugernum=0
    friesnum=0
    chickennum=0
    colanum=0
    mealnum=0
    disoff=1
    meal=''
    price.set(total)
    disc.set(1)

#金額欄位
price=tk.StringVar()
tk.Label(window,text="金額:").grid(row=1,column=1,padx=2,pady=5)
tk.Entry(window,width=10,textvariable=price,state="readonly").grid(row=1,column=2,padx=2,pady=5)

#餐點選單
tk.Button(window,text="漢堡\n$20",width=10,height=5,command=lambda:order('hambuger',20)).grid(row=2,column=1,padx=2,pady=5)
tk.Button(window,text="薯條\n$15",width=10,height=5,command=lambda:order('fries',15)).grid(row=2,column=2,padx=2,pady=5)
tk.Button(window,text="雞塊\n$25",width=10,height=5,command=lambda:order('chicken',25)).grid(row=2,column=3,padx=2,pady=5)
tk.Button(window,text="可樂\n$5",width=10,height=5,command=lambda:order('cola',5)).grid(row=2,column=4,padx=2,pady=5)

#折扣
disc=tk.StringVar()
disc.set(1)
tk.Label(window,text="折扣:").grid(row=3,column=1,padx=2,pady=5)
tk.Radiobutton(window,text="沒有折扣",value="1",variable=disc,command=lambda:discount(1)).grid(row=3,column=2,padx=2,pady=5)
tk.Radiobutton(window,text="85折",value="0.85",variable=disc,command=lambda:discount(0.85)).grid(row=3,column=3,padx=2,pady=5)
tk.Radiobutton(window,text="75折",value="0.75",variable=disc,command=lambda:discount(0.75)).grid(row=3,column=4,padx=2,pady=5)
tk.Radiobutton(window,text="5折",value="0.5",variable=disc,command=lambda:discount(0.5)).grid(row=3,column=5,padx=2,pady=5)


#結帳與重新點餐
tk.Button(window,text="結帳",width=10,height=1,command=accept).grid(row=4,column=1,padx=2,pady=5)
tk.Button(window,text="重新點餐",width=10,height=1,command=reset).grid(row=4,column=2,padx=2,pady=5)


window.mainloop()
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 13:00:49 2020

@author: K0718
"""

import tkinter as tk
window = tk.Tk()
window.title("單選按鈕")
window.geometry('500x500')



#menu
menuBar=tk.Menu(window)


def start():
    label.config(text="開始新遊戲")
    
def cheat():
    label.config(text="作幣指令")

def gameset():
    label.config(text="遊戲設定")

def screenset():
    label.config(text="畫面設定")

def opt():
    label.config(text="遊戲優化MAX")
    
def attact():
    label.config(text="攻擊所有敵人")
 
#關閉視窗
def close_window():
     window.destroy()

#建立第一個選單與其子選單
fileMenu = tk.Menu(menuBar,tearoff=False)
fileMenu.add_command(label="開始新遊戲",command=start)
fileMenu.add_command(label="作幣指令",command=cheat)
fileMenu.add_separator()
fileMenu.add_command(label="EXIT",command = close_window)
menuBar.add_cascade(label="檔案 ",menu=fileMenu)


#建立第二個選單與其子選單
fileMenu2 = tk.Menu(menuBar,tearoff=False)
fileMenu2.add_command(label="遊戲設定",command=gameset)
fileMenu2.add_command(label="畫面設定",command=screenset)
menuBar.add_cascade(label="選項 ",menu=fileMenu2)


#建立第二個選單的第三層選單
submenu = tk.Menu(fileMenu2,tearoff=False)
submenu.add_command(label="遊戲優化MAX",command=opt)
submenu.add_command(label="攻擊所有敵人",command=attact)
fileMenu2.add_cascade(label="進階遊戲設定",menu=submenu)

window.config(menu=menuBar)




#radiobutton

string = tk.StringVar()
gender=tk.StringVar()

def selection():
    label.config(text="我是"+gender.get()+"我喜歡" + string.get())
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
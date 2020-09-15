# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 10:18:14 2020

@author: K0718
"""

#建立視窗
import tkinter as tk
window = tk.Tk()
window.title("menubar")
window.geometry('500x500')
menuBar=tk.Menu(window)



#建立第一個選單與子選單
fileMenu = tk.Menu(menuBar,tearoff=False)
fileMenu.add_command(label="開始新遊戲")
fileMenu.add_command(label="作幣指令")
fileMenu.add_separator()
fileMenu.add_command(label="EXIT")
menuBar.add_cascade(label="檔案 ",menu=fileMenu)


#建立第二個選單與子選單
fileMenu2 = tk.Menu(menuBar,tearoff=False)
fileMenu2.add_command(label="遊戲設定")
fileMenu2.add_command(label="畫面設定")
menuBar.add_cascade(label="選項 ",menu=fileMenu2)


#建立第二個選單的第三層選單
submenu = tk.Menu(fileMenu2,tearoff=False)
submenu.add_command(label="遊戲優化MAX")
submenu.add_command(label="攻擊所有敵人")
fileMenu2.add_cascade(label="進階遊戲設定",menu=submenu)

window.config(menu=menuBar)
window.mainloop()





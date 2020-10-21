# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 08:12:52 2020

@author: K0718
"""

from pytube import YouTube
import tkinter as tk
window=tk.Tk()
window.title("Youtube下載器")
window.geometry("500x500")
window.resizable(False,False)


progress=0        
def showProgress(stream,chunk,bytes_remaining):
    size=stream.filesize
    global progress
    preProgress = progress
    
    currentProgress=int((size-bytes_remaining)*100/size)
    progress=currentProgress
    
    if progress == 100:
        print("下載完成")
        return
    
    if preProgress != progress:
        scale.set(progress)
        window.update()
        print("目前進度"+ str(currentProgress)+"%")

def onClick():
    global var
    var.set(entry.get())
    try:
       yt=YouTube(var.get(),on_progress_callback=showProgress)
       stream=yt.streams.first()
       stream.download()
    except:
        print("下載失敗")



label=tk.Label(window,text="請輸入網址")
label.pack()

var=tk.StringVar()

entry=tk.Entry(window,width=50)
entry.pack()

button=tk.Button(window,text="下載",command=onClick)
button.pack()

scale=tk.Scale(window,label="進度條",from_=0,to=100,orient=tk.HORIZONTAL,length=200,showvalue=False,tickinterval=0)
scale.pack()

window.mainloop()
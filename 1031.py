# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 09:43:01 2020

@author: K0718
"""
from pytube import YouTube
import tkinter as tk
import threading
window=tk.Tk()
window.title("Youtube下載器")
window.geometry("500x150")
window.resizable(False,False)



def thread():
    threading.Thread(target=onClick).start()

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
    var.set(entry.get())#將entry的值設定給var
    button.config(state=tk.DISABLED)
    try:
        yt = YouTube(var.get(),on_progress_callback=showProgress)
        if onlyMusic.get():
            stream=yt.streams.filter(only_audio=True).first()
            stream.download()
        else:
            stream=yt.streams.first()
            stream.download()
    except:
        button.config(state=tk.NORMAL)
        print("下載失敗")



    
var=tk.StringVar()
entry=tk.Entry(window,width=50)
entry.pack()

onlyMusic=tk.BooleanVar()
check=tk.Checkbutton(window,text="只有音樂",variable=onlyMusic,onvalue=True,offvalue=False)
check.pack()

button=tk.Button(window,text="下載",command=thread)
button.pack()

scale=tk.Scale(window,label="進度條",from_=0,to=100,orient=tk.HORIZONTAL,length=200,showvalue=False,tickinterval=0)
scale.pack()

window.mainloop()


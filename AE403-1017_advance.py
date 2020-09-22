# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 08:14:18 2020

@author: K0718
"""
from pytube import YouTube
import tkinter as tk








window = tk.Tk()
ys = tk.StringVar()
window.iconbitmap("C:\\Users\\K0718\\Desktop\\py\\test.ico")#視窗左上角圖示
window.title("Youtube downloader")
window.geometry("500x500")

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
        print("目前進度"+ str(currentProgress)+"%")

def download():   
    url=ys.get()#取得使用者輸入的納址
    yt = YouTube(url,on_progress_callback=showProgress)
    stream=yt.streams.first()
    #stream = yt.streams.filter(res="720p").first()
    stream.download("C:\\Users\\K0718\\Desktop\\py",yt.title)#存檔路徑、存檔名稱


    


label = tk.Label(window,text="Youtube下載器")
label.pack()

entry = tk.Entry(window,textvariable=ys,width=30)
entry.pack()

button = tk.Button(window,text="下載",command=download)#按下下載鈕下載youtube網址內容
button.pack()

window.mainloop()




"""import tkinter as tk
window=tk.Tk()
window.title("GUI")
window.geometry("500x500")
window.iconbitmap("C:\\Users\\K0718\\Desktop\\py\\test.ico")

window.mainloop()"""
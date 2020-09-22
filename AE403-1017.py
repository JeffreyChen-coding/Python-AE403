# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:07:38 2020


"""

from pytube import YouTube
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
    

yt = YouTube("https://www.youtube.com/watch?v=XZkwdI8-zsU",on_progress_callback=showProgress)
stream = yt.streams.first()
stream.download("C:\\Users\\K0718\\Desktop\\py",yt.title)


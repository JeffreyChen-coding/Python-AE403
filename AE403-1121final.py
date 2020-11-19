# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:15:58 2020


"""

import turtle
import time
import datetime
tur=turtle.Turtle()
tur.speed(3)


#畫時鐘圓框
tur.hideturtle()
tur.penup()
tur.goto(0,-200)
tur.pendown()
tur.circle(210)


tur.penup()
tur.goto(0,0)
tur.pendown()

#寫時鐘刻度
def writenum(num):
    tur.penup()
    tur.forward(200)
    tur.write(num)
    tur.back(200)
    tur.pendown()
tur.seth(90)   
for i in range(1,13):
    tur.right(30)
    writenum(i)

#是否要更新時針和分針
update = True

#是否要更新秒針
updatesecond = True

while True:
    
    #現在時間
    now = datetime.datetime.now()
    h = now.hour % 12
    m = now.minute
    s = now.second
    
    #更新時針和分針
    if update:
        hour=turtle.Turtle()
        hour.seth(90)
        hour.right(h*30+m/60*30)
        hour.forward(70)
        
        minute=turtle.Turtle()
        minute.seth(90)
        minute.right(m * 6)
        minute.forward(130)
        update = False
    
    #更新秒針
    if updatesecond:
        second=turtle.Turtle()
        second.seth(90)
        second.right(s*6)
        second.forward(150)
        updatesecond = False
    
    #取得隔1秒後的時間
    time.sleep(1)
    now = datetime.datetime.now()
    mNew = now.minute
    sNew = now.hour 
    
    #先清空秒針再重新繪製秒針
    updatesecond = True
    second.clear()
    second.reset()
    
    #分鐘不等於現在的分鐘時，先清空時針和分針，再重新繪置時針和分針
    if mNew != m:
          update = True 
          #清除畫布，並重置
          hour.clear() 
          hour.reset()
          #清除畫布，並重置
          minute.clear()
          minute.reset()
          
    
        
turtle.done()
turtle.exitonclick()

# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 09:29:14 2020

"""

import turtle
import time
import datetime
tur=turtle.Turtle()

tur.speed(0)#0表示最科，10表示快，1表示最慢 If input is a number greater than 10 or smaller than 0.5, speed is set to 0

turtle.setup(800,800)

def writeNumber(num):
    tur.penup()
    tur.forward(300)
    tur.write(num)
    tur.back(300)
    tur.pendown()

tur.seth(90)    

for i in range(1,13):
    tur.right(30)
    writeNumber(i)

#控制是否要更新時間(時針/分針)
update = True 
#控制是否要更新時間(秒針)
updateSecond = True 

while True:
      #取得時間時(12進制)/分/秒
      now = datetime.datetime.now()
      h = now.hour % 12
      m = now.minute
      s = now.second
      
      if update:
          #繪畫時針
          hour = turtle.Turtle()
          #將Turtle轉向北方
          hour.seth(90) 
          #一圈12小時(30度/小時)
          #分鐘也會影響時針，每60分鐘影響30度(0.5度/分鐘)
          hour.right(h * 30 + m / 60 * 30)
          hour.forward(140)

          #繪畫分針
          minute = turtle.Turtle()
          #將Turtle轉向北方
          minute.seth(90)
          #6度/分鐘
          minute.right(m * 6)
          minute.forward(200)
          #由於繪畫完畢，update為False
          update = False
            
      if updateSecond:
          #繪畫秒針
          second = turtle.Turtle()
          #將Turtle轉向北方
          second.seth(90) 
          #6度/秒鐘
          second.right(s * 6)
          second.forward(220)
          #由於繪畫完畢，updateSecond為False
          updateSecond = False

      time.sleep(1)
      now = datetime.datetime.now()
      mNew = now.minute
      sNew = now.hour 
      

      if mNew != m: #秒針指到12時(60秒)，時針和分針重置，例如原本為56分，當秒針指到12時，變成57分，時針和秒針重置
          update = True 
          #清除畫布，並重置
          hour.clear() 
          hour.reset()
          #清除畫布，並重置
          minute.clear()
          minute.reset()
      if mNew != s:
          updateSecond = True
          #清除畫布，並重置
          second.clear()
          second.reset()

turtle.done()
turtle.exitonclick()
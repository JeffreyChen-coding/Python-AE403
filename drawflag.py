# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 13:23:04 2020

"""

import turtle
import tkinter as tk
window=tk.Tk()
window.geometry("600x600")
tur=turtle.Turtle()
turd=turtle.Turtle()
turf=turtle.Turtle()
turi=turtle.Turtle()
def drawtaiwan():    
   
    tur.clear()
    tur.reset()
    turd.clear()
    turd.reset()
    turf.clear()
    turf.reset()
    turi.clear()
    turi.reset()
    turtle.setup(800,800)
    tur.speed(10)
    tur.hideturtle()
    def draw():
        tur.forward(400)
        tur.right(90)
        tur.forward(300)
        tur.right(90)
        tur.forward(400)
        tur.right(90)
        tur.forward(300)
        tur.right(90)
    

    def draw1():
        tur.forward(180)
        tur.right(90)
        tur.forward(130)
        tur.right(90)
        tur.forward(180)
        tur.right(90)
        tur.forward(130)
        tur.right(90)


    #畫紅色長方型
    tur.penup()
    tur.goto(-100,100)
    tur.pendown()
    tur.fillcolor("#ff0000")
    tur.begin_fill()
    draw()
    tur.end_fill()


    #畫藍色長方形
    tur.penup()
    tur.goto(-100,100)
    tur.pendown()
    tur.fillcolor("#003377")
    tur.begin_fill()
    draw1()
    tur.end_fill()


    #畫十二芒星
    tur.seth(15)
    tur.penup()
    tur.pencolor("#ffffff")
    tur.goto(35,62)
    tur.pendown()
    tur.fillcolor("#ffffff")
    tur.begin_fill()
    for i in range(12):
        tur.right(150)
        tur.forward(110)
   
    tur.end_fill()


    #畫圓
    tur.penup()
    tur.goto(-7,5)
    tur.pensize("5")
    tur.pencolor("#003377")
    tur.pendown()
    tur.fillcolor("#ffffff")
    tur.begin_fill()
    tur.circle(29)
    tur.end_fill()




def drawgermany():
    tur.clear()
    tur.reset()
    turd.clear()
    turd.reset()
    turf.clear()
    turf.reset()
    turi.clear()
    turi.reset()
    turtle.setup(800,800)
    turd.speed(10)
    turd.hideturtle()
    def black():
        turd.penup()
        turd.goto(-100,100)
        turd.pendown()
        turd.fillcolor("#000000")
        turd.begin_fill()
        turd.forward(400)
        turd.right(90)
        turd.forward(80)
        turd.right(90)
        turd.forward(400)
        turd.right(90)
        turd.forward(80)
        turd.right(90)
        turd.end_fill()
        
    def red():
        turd.penup()
        turd.goto(-100,20)
        turd.pendown()
        turd.fillcolor("#ff0000")
        turd.begin_fill()
        turd.forward(400)
        turd.right(90)
        turd.forward(80)
        turd.right(90)
        turd.forward(400)
        turd.right(90)
        turd.forward(80)
        turd.right(90)
        turd.end_fill()
        
    def yellow():
        turd.penup()
        turd.goto(-100,-60)
        turd.pendown()
        turd.fillcolor("#ffff00")
        turd.begin_fill()
        turd.forward(400)
        turd.right(90)
        turd.forward(80)
        turd.right(90)
        turd.forward(400)
        turd.right(90)
        turd.forward(80)
        turd.right(90)
        turd.end_fill()
    black()
    red()
    yellow()


def drawfrance():
    tur.clear()
    tur.reset()
    turd.clear()
    turd.reset()
    turf.clear()
    turf.reset()
    turi.clear()
    turi.reset()
    turtle.setup(800,800)
    turf.speed(10)
    turf.hideturtle()
    def blue():
        turf.penup()
        turf.goto(-100,100)
        turf.pendown()
        turf.fillcolor("#0000ff")
        turf.begin_fill()
        turf.forward(80)
        turf.right(90)
        turf.forward(150)
        turf.right(90)
        turf.forward(80)
        turf.right(90)
        turf.forward(150)
        turf.right(90)
        turf.end_fill()
        
    def white():
        turf.penup()
        turf.goto(-20,100)
        turf.pendown()
        turf.fillcolor("#ffffff")
        turf.begin_fill()
        turf.forward(80)
        turf.right(90)
        turf.forward(150)
        turf.right(90)
        turf.forward(80)
        turf.right(90)
        turf.forward(150)
        turf.right(90)
        turf.end_fill()
        
    def red():
        turf.penup()
        turf.goto(60,100)
        turf.pendown()
        turf.fillcolor("#ff0000")
        turf.begin_fill()
        turf.forward(80)
        turf.right(90)
        turf.forward(150)
        turf.right(90)
        turf.forward(80)
        turf.right(90)
        turf.forward(150)
        turf.right(90)
        turf.end_fill()
    blue()
    white()
    red() 

def drawitaly():
    tur.clear()
    tur.reset()
    turd.clear()
    turd.reset()
    turf.clear()
    turf.reset()
    turi.clear()
    turi.reset()
    turtle.setup(800,800)
    turi.speed(10)
    turi.hideturtle()
    def green():
        turi.penup()
        turi.goto(-100,100)
        turi.pendown()
        turi.fillcolor("#00A600")
        turi.begin_fill()
        turi.forward(80)
        turi.right(90)
        turi.forward(150)
        turi.right(90)
        turi.forward(80)
        turi.right(90)
        turi.forward(150)
        turi.right(90)
        turi.end_fill()
        
    def white():
        turi.penup()
        turi.goto(-20,100)
        turi.pendown()
        turi.fillcolor("#ffffff")
        turi.begin_fill()
        turi.forward(80)
        turi.right(90)
        turi.forward(150)
        turi.right(90)
        turi.forward(80)
        turi.right(90)
        turi.forward(150)
        turi.right(90)
        turi.end_fill()
        
    def red():
        turi.penup()
        turi.goto(60,100)
        turi.pendown()
        turi.fillcolor("#ff0000")
        turi.begin_fill()
        turi.forward(80)
        turi.right(90)
        turi.forward(150)
        turi.right(90)
        turi.forward(80)
        turi.right(90)
        turi.forward(150)
        turi.right(90)
        turi.end_fill()
    green()
    white()
    red()
    





tk.Button(window,text="Taiwan",command=drawtaiwan).pack(side="left")
tk.Button(window,text="Germany",command=drawgermany).pack(side="top")
tk.Button(window,text="France",command=drawfrance).pack(side="right")
tk.Button(window,text="Italy",command=drawitaly).pack(side="bottom")
turtle.done()
turtle.exitonclick() 

window.mainloop()

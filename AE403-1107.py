# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 09:29:20 2020

"""

import turtle
tur=turtle.Turtle()

turtle.setup(850,850)



def Frence():
    tur.begin_fill()
    tur.forward(50)
    tur.right(90)
    tur.forward(100)
    tur.right(90)
    tur.forward(50)
    tur.right(90)
    tur.forward(100)
    tur.right(90)
    tur.end_fill()
    
def Germany():
    tur.begin_fill()
    tur.forward(200)
    tur.right(90)
    tur.forward(50)
    tur.right(90)
    tur.forward(200)
    tur.right(90)
    tur.forward(50)
    tur.right(90)  
    tur.end_fill()

#Frence
tur.penup()
tur.goto(-400,400)
tur.pendown()
tur.fillcolor(0,0,1)
Frence()


tur.penup()
tur.goto(-350,400)
tur.pendown()
tur.fillcolor(1,1,1)
Frence()


tur.penup()
tur.goto(-300,400)
tur.pendown()
tur.fillcolor(1,0,0)
Frence()



#Germany
tur.penup()
tur.goto(-400,250)
tur.pendown()
tur.fillcolor(0,0,0)
Germany()


tur.penup()
tur.goto(-400,200)
tur.pendown()
tur.fillcolor(1,0,0)
Germany()


tur.penup()
tur.goto(-400,150)
tur.pendown()
tur.fillcolor(1,1,0)
Germany()





turtle.done()
turtle.exitonclick()
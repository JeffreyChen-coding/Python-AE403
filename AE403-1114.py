# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 08:42:19 2020

@author: K0718
"""

import turtle
tur=turtle.Turtle()

tur.penup()
tur.forward(100)
tur.write(1)
tur.back(100)
tur.pendown()


#m=1  m=(y1-y2)/(x1-x2)
tur.penup()
tur.goto(0,0)
tur.pendown()
tur.goto(100,100)


#m<1  y=mx+b  以x為主
tur.penup()
tur.goto(0,0)
tur.pendown()
tur.goto(100,75)


#m>1 y=mx+b  以y為主
tur.penup()
tur.goto(0,0)
tur.pendown()
tur.goto(75,100)


turtle.done()
turtle.exitonclick()
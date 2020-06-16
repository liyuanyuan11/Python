from turtle import *
def setting():
    setup(800,500)
    pensize(4)
    hideturtle()
    colormode(255)
    speed(10)
def nose():
    penup()
    goto(-100,100)
    setheading(-30)
    color((255,155,192),"pink")
    pendown()
    begin_fill()
    segment=0.4
    for i in range(120):
        if 0<=i<30 or 60<=i<90:
            segment=segment+0.08
            left(3)
            forward(segment)
        else:
            segment=segment-0.08
            left(3)
            forward(segment)
    end_fill()
    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    color((255,155,192),(160,82,45))
    pendown()
    begin_fill()
    circle(5)
    end_fill()
    penup()
    setheading(0)
    forward(20)
    pendown()
    begin_fill()
    circle(5)
    end_fill()

import turtle
turtle.pendown()
segment=1
for i in range(120):
    if 0<=i<30 or 60<=i<90:
        segment=segment+0.2
        turtle.left(3)
        turtle.forward(segment)
    else:
        segment=segment-0.2
        turtle.left(3)
        turtle.forward(segment)        
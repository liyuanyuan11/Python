import turtle
turtle.speed(10)
for x in range(100):
    turtle.forward(x)
    turtle.left(90) 
turtle.penup()
turtle.goto(-200,200)
turtle.pendown()
for x in range(100):
    turtle.forward(x)
    turtle.left(90)
turtle.penup()
turtle.goto(200,200)
turtle.pendown()
for x in range(100):
    turtle.forward(x)
    turtle.left(90)
turtle.penup()
turtle.goto(-200,-200)
turtle.pendown()
for x in range(100):
    turtle.forward(x)
    turtle.left(90)
turtle.penup()
turtle.goto(200,-200)
turtle.pendown()
for x in range(100):
    turtle.forward(x)
    turtle.left(90)

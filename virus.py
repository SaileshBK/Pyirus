import turtle

wn = turtle.Screen()
wn.bgcolor('black')
turtle.speed(600)
x = 200
while x > 0:
    if (x % 2) == 0:
        turtle.color('cyan')
    else:
        turtle.color('green')
    turtle.left(x)
    turtle.forward(x * 2)
    x = x - 1
turtle.up()
turtle.left(75)    
turtle.forward(700)
turtle.down()
x = 200
while x > 0:
    if (x % 2) == 0:
        turtle.color('green')
    else:
        turtle.color('cyan')
    turtle.left(x)
    turtle.forward(x * 2)
    x = x - 1

wn.exitonclick()
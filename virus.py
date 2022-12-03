import turtle

wn = turtle.Screen()
wn.bgcolor('black')
turtle.speed(600)
for x in range(200, 0, -1):
    if (x % 2) == 0:
        turtle.color('cyan')
    else:
        turtle.color('green')
    turtle.left(x)
    turtle.forward(x * 2)
turtle.up()
turtle.left(75)
turtle.forward(700)
turtle.down()
for x in range(200, 0, -1):
    if (x % 2) == 0:
        turtle.color('green')
    else:
        turtle.color('cyan')
    turtle.left(x)
    turtle.forward(x * 2)
wn.exitonclick()
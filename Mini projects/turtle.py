import turtle

color = ['red', 'green', 'yellow', 'blue']
turtle.speed(0)
turtle.pensize(4)

for i in range(200):
    turtle.color(color[i % 4])
    turtle.forward(i * 2)
    turtle.left(89)

turtle.done()

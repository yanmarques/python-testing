import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    x = turtle.Turtle()
    x.speed(2)

    i = 90
    while True:

        for z in range(0, 4):
            x.forward(60)
            x.right(90)
            x.forward(60)
            x.right(90)
            x.forward(60)
            x.right(90)
            x.forward(60)
            x.right(95)
            
        for w in range(0, 4):
            x.forward(60)
            x.right(95)
            x.forward(60)
            x.right(95)
            x.forward(60)
            x.right(95)
            x.forward(60)
            x.right(95)

draw_square()

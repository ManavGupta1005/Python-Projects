import turtle

t1 = turtle.Turtle()
t1.screen.bgcolor("black")
t1.pensize(2)
t1.color("red")

t1.left(90)
t1.backward(100)
t1.speed(10000000000000)
t1.shape('classic')


def tree(i):
    if i < 10:
        return
    else:
        t1.forward(i)
        t1.color("purple")
        t1.circle(2)
        t1.color("brown")
        t1.left(30)
        tree(3 * i / 4)
        t1.right(60)
        tree(3 * i / 4)
        t1.left(30)
        t1.backward(i)


tree(100)
turtle.done()



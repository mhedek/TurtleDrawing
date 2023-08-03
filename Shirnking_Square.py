import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Shirinking Square")

turtle_instance = turtle.Turtle()
turtle_instance.color("brown")

def shirnkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.right(90)
        size = size - 5

shirnkingSquare(150)
shirnkingSquare(130)
shirnkingSquare(110)
shirnkingSquare(90)
shirnkingSquare(70)
shirnkingSquare(50)
shirnkingSquare(30)
shirnkingSquare(10)

turtle.done()
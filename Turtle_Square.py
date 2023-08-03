import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("pink")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()

for i in range(4):
    turtle_instance.forward(180)
    turtle_instance.left(90)

turtle.done()
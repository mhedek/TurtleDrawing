import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("pink")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()
for i in range(5):
    turtle_instance.left(144)
    turtle_instance.forward(300)

turtle.done()
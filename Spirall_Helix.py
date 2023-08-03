import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Helix")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")
turtle.speed("fastest")
turtle_color = ["red", "blue", "pink", "green", "purple", "yellow"]

for i in range(15):
    turtle_instance.color(turtle_color[i % 6])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)

turtle.mainloop()
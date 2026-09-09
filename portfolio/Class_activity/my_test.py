import turtle
my_turtle = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("My First Turtle Program")
my_turtle.shape("turtle")
my_turtle.color("blue")
for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)
my_turtle.penup()
my_turtle.goto(150, 0)
my_turtle.pendown()
for i in range(3):
    my_turtle.forward(100)
    my_turtle.right(120)
for i in range(5, 10, 2):
    print(i)
print(list(range(2, 6)))
window.exitonclick()
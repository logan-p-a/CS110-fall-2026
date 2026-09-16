import turtle
t = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("lightblue")
t.color("green")
sides = int(input("Enter the number of sides for the shape: "))
angle = 360 / sides
for i in range(sides):
    t.forward(20)
    t.left(angle)
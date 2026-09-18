import turtle  # 1. import modules
import random

# Part A
window = turtle.Screen()  # 2.  Create a screen
window.bgcolor("lightblue")

michelangelo = turtle.Turtle()  # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color("orange")
leonardo.color("blue")
michelangelo.shape("turtle")
leonardo.shape("turtle")

michelangelo.up()  # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

## 5. Your PART A code goes here
m_distance = random.randint(1, 101)
michelangelo.forward(m_distance)
l_distance = random.randint(1, 101)
leonardo.forward(l_distance)

michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

for i in range(10):
    m_distance = random.randint(1, 11)
    michelangelo.forward(m_distance)
    l_distance = random.randint(1, 11)
    leonardo.forward(l_distance)

michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)
# PART B - complete part B here
leonardo.down()
for i in range(3):
    leonardo.forward(50)
    leonardo.left(360/3)
leonardo.clear()
for i in range(4):
    leonardo.forward(50)
    leonardo.left(360/4)
leonardo.clear()
for i in range(6):
    leonardo.forward(50)
    leonardo.left(360/6)
leonardo.clear()
for i in range(20):
    leonardo.forward(50)
    leonardo.left(360/20)
leonardo.clear()
for i in range(100):
    leonardo.forward(10)
    leonardo.left(360/100)
leonardo.clear()
leonardo.speed(0)
for i in range(360):
    leonardo.forward(2)
    leonardo.left(360/360)
leonardo.clear()

window.exitonclick()

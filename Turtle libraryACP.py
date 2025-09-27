import turtle

# creating canvas
turtle.Screen().bgcolor("Orange")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome to Turtle Window")

# turtle object creation
board = turtle.Turtle()

# creating a square
for i in range(4):
    board.forward(100)
    board.left(90)
    i = i+1
    
turtle.Screen().bgcolor("Orange")
board = turtle.Turtle()

board.forward(100)  

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

t = turtle.Turtle()
t.speed(1)

width = 200
height = 100

for _ in range(2):
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)



t = turtle.Turtle()
t.speed(1)

sides = 6
length = 100
angle = 360 / sides

for _ in range(sides):
    t.forward(length)
    t.left(angle)





turtle.done

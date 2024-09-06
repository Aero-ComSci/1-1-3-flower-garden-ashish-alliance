import turtle as trtl

def draw_stem(painter, color="green", size=15):
    painter.color(color)
    painter.pensize(size)
    painter.goto(0, -150)
    painter.setheading(90)
    painter.forward(100)
    painter.setheading(270)
    painter.circle(20, 120, 20)
    painter.setheading(90)
    painter.goto(0, -60)
    painter.forward(60)
    painter.setheading(0)

def draw_tulip(painter, x, y):
    draw_stem(painter)
    painter.penup()
    painter.shape("circle")
    painter.turtlesize(2)
    painter.color("darkorchid")
    painter.goto(x, y)

    for petal in range(18):
        painter.right(20)
        painter.forward(30)
        painter.stamp()

    painter.goto(x, y - 30)
    painter.color("blue")

    for petal in range(12):
        painter.right(30)
        painter.forward(30)
        painter.stamp()

def draw_rose(painter, x, y):
    painter.color("red")
    painter.pensize(3)
    painter.penup()
    painter.goto(x, y)
    painter.pendown()

    def draw_petal():
        painter.circle(50, 60)
        painter.left(120)
        painter.circle(50, 60)
        painter.left(120)

    for _ in range(6):
        draw_petal()
        painter.right(60)

    draw_stem(painter)

def draw_sunflower(painter, x, y):
    draw_stem(painter)
    painter.penup()
    painter.shape("circle")
    painter.turtlesize(2)
    painter.color("yellow")
    painter.goto(x, y)

    for petal in range(18):
        painter.right(20)
        painter.forward(30)
        painter.stamp()

    painter.goto(x, y - 30)
    painter.color("brown")

    for petal in range(12):
        painter.right(30)
        painter.forward(30)
        painter.stamp()

def draw_lily(painter, x, y):
    painter.color("green")
    painter.pensize(5)
    painter.penup()
    painter.goto(x, y)
    painter.pendown()

    def draw_petal():
        painter.circle(50, 60)
        painter.left(120)
        painter.circle(50, 60)
        painter.left(120)

    for _ in range(6):
        painter.begin_fill()
        draw_petal()
        painter.end_fill()
        painter.right(60)

def draw_violet(painter, x, y):
    painter.color("purple")
    painter.pensize(3)
    painter.penup()
    painter.goto(x, y)
    painter.pendown()

    def draw_petal():
        painter.circle(50, 60)
        painter.left(120)
        painter.circle(50, 60)
        painter.left(120)

    for _ in range(6):
        painter.begin_fill()
        draw_petal()
        painter.end_fill()
        painter.right(60)

    draw_stem(painter)

# Get user input
userinput = input("I draw flowers. What flower and how many would you like me to draw?").strip()
flower_choice = userinput.split(" ")
flower_type = None
num = 0

# Process user input
for word in flower_choice:
    if word.isdigit():
        num = int(word)
        if num > 30:
            print("Our max on one run is 30. Sorry for this and thank you for understanding.")
            num = 30
        break

if num == 0:
    num = 1  # Default to 1 if no number is provided

flowers = ["roses", "tulips", "violets", "lilies", "sunflower"]

for word in flower_choice:
    if word.lower() in flowers:
        flower_type = word.lower()
        break

if flower_type is None:
    print("Invalid flower type. Please choose from: roses, tulips, violets, lilies, sunflower.")
else:
    # Set up the screen and turtle
    screen = trtl.Screen()
    screen.bgcolor("white")
    painter = trtl.Turtle()
    painter.speed(0)

    # Draw flowers
    x_start, y_start = -200, 200
    x_offset, y_offset = 100, -100
    for i in range(num):
        if flower_type == "tulips":
            draw_tulip(painter, x_start + i * x_offset, y_start + i * y_offset)
        elif flower_type == "roses":
            draw_rose(painter, x_start + i * x_offset, y_start + i * y_offset)
        elif flower_type == "sunflower":
            draw_sunflower(painter, x_start + i * x_offset, y_start + i * y_offset)
        elif flower_type == "lilies":
            draw_lily(painter, x_start + i * x_offset, y_start + i * y_offset)
        elif flower_type == "violets":
            draw_violet(painter, x_start + i * x_offset, y_start + i * y_offset)

    # Hide turtle and finish
    painter.hideturtle()
    screen.mainloop()

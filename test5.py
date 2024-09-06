import turtle as trtl

def draw_stem(painter, color="green", size=20, length=150):
    painter.color(color)
    painter.pensize(size)
    painter.penup()
    painter.goto(0, -150)  # Positioning the turtle to start the stem
    painter.setheading(90)  # Point upwards
    painter.pendown()
    painter.forward(length)
    painter.setheading(180)
    painter.circle(20, 180)  # Curve at the bottom
    painter.setheading(0)  # Reset heading

def draw_petal(painter, petal_color, petal_count, petal_size):
    painter.color(petal_color)
    painter.pendown()
    for _ in range(petal_count):
        painter.forward(petal_size)
        painter.stamp()
        painter.right(360 / petal_count)
    painter.penup()

def draw_tulip(painter, x, y):
    draw_stem(painter, size=20, length=150)
    painter.penup()
    painter.shape("circle")
    painter.turtlesize(2)
    painter.goto(x, y)
    painter.setheading(0)
    draw_petal(painter, "darkorchid", 18, 30)
    painter.goto(x, y - 30)
    draw_petal(painter, "blue", 12, 30)

def draw_sunflower(painter, x, y):
    draw_stem(painter, size=20, length=150)
    painter.penup()
    painter.shape("circle")
    painter.turtlesize(2)
    painter.goto(x, y)
    painter.setheading(0)
    draw_petal(painter, "yellow", 18, 30)
    painter.goto(x, y - 30)
    draw_petal(painter, "brown", 12, 30)

def draw_rose(painter, x, y):
    painter.color("red")
    painter.pensize(3)
    painter.penup()
    painter.goto(x, y)
    painter.pendown()

    def draw_rose_petal():
        painter.circle(50, 60)
        painter.left(120)
        painter.circle(50, 60)
        painter.left(120)

    for _ in range(6):
        draw_rose_petal()
        painter.right(60)

    draw_stem(painter, size=15, length=100)

def draw_lily(painter, x, y):
    painter.color("green")
    painter.pensize(5)
    painter.penup()
    painter.goto(x, y)
    painter.pendown()

    def draw_lily_petal():
        painter.circle(50, 60)
        painter.left(120)
        painter.circle(50, 60)
        painter.left(120)

    for _ in range(6):
        painter.begin_fill()
        draw_lily_petal()
        painter.end_fill()
        painter.right(60)

    draw_stem(painter, size=20, length=150)

def draw_violet(painter, x, y):
    painter.color("purple")
    painter.pensize(3)
    painter.penup()
    painter.goto(x, y)
    painter.pendown()

    def draw_violet_petal():
        painter.circle(50, 60)
        painter.left(120)
        painter.circle(50, 60)
        painter.left(120)

    for _ in range(6):
        painter.begin_fill()
        draw_violet_petal()
        painter.end_fill()
        painter.right(60)

    draw_stem(painter, size=20, length=150)

# Get user input
userinput = input("I draw flowers. What flower and how many would you like me to draw? (e.g., 3 tulips)").strip()
flower_choice = userinput.split()
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

flowers = ["roses", "tulips", "violets", "lilies", "sunflowers"]

for word in flower_choice:
    if word.lower() in flowers:
        flower_type = word.lower()
        break

if flower_type is None:
    print("Invalid flower type. Please choose from: roses, tulips, violets, lilies, sunflowers.")
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
        position_x = x_start + i * x_offset
        position_y = y_start + i * y_offset
        if flower_type == "tulips":
            draw_tulip(painter, position_x, position_y)
        elif flower_type == "roses":
            draw_rose(painter, position_x, position_y)
        elif flower_type == "sunflowers":
            draw_sunflower(painter, position_x, position_y)
        elif flower_type == "lilies":
            draw_lily(painter, position_x, position_y)
        elif flower_type == "violets":
            draw_violet(painter, position_x, position_y)

    # Hide turtle and finish
    painter.hideturtle()
    screen.mainloop()

import turtle as trtl

def draw_stem(painter, start_x, start_y, color="green", size=5, length=100):
    # Draw the stem
    painter.color(color)
    painter.pensize(size)
    painter.penup()
    painter.goto(start_x, start_y)
    painter.pendown()
    painter.setheading(90)  # Point upwards
    painter.begin_fill()
    painter.forward(length)
    painter.right(90)
    painter.circle(10, 180)  # Curve at the top
    painter.right(90)
    painter.forward(length)
    painter.right(90)
    painter.circle(10, 180)  # Curve at the bottom
    painter.right(90)
    painter.end_fill()
    
    # Draw leaves
    painter.penup()
    painter.goto(start_x + 10, start_y - length * 0.6)  # Position for the first leaf
    painter.pendown()
    painter.color("darkgreen")
    painter.begin_fill()
    painter.setheading(45)
    painter.circle(30, 90)  # Leaf shape
    painter.left(90)
    painter.circle(30, 90)  # Complete the leaf
    painter.end_fill()
    
    painter.penup()
    painter.goto(start_x - 10, start_y - length * 0.6)  # Position for the second leaf
    painter.pendown()
    painter.begin_fill()
    painter.setheading(135)
    painter.circle(30, 90)  # Leaf shape
    painter.left(90)
    painter.circle(30, 90)  # Complete the leaf
    painter.end_fill()

def draw_tulip(painter, x, y):
    # Draw stem for the tulip
    draw_stem(painter, x, y - 150)

    painter.penup()
    painter.shape("circle")
    painter.turtlesize(2)
    painter.color("darkorchid")
    painter.goto(x, y)

    painter.pendown()
    for petal in range(18):
        painter.right(20)
        painter.forward(30)
        painter.stamp()

    painter.penup()
    painter.goto(x, y - 30)
    painter.color("blue")
    painter.pendown()
    for petal in range(12):
        painter.right(30)
        painter.forward(30)
        painter.stamp()

def draw_rose(painter, x, y):
    painter.penup()
    painter.goto(x, y)
    painter.pendown()
    painter.color("red")
    painter.pensize(3)

    def draw_petal():
        painter.circle(50, 60)
        painter.left(120)
        painter.circle(50, 60)
        painter.left(120)

    for _ in range(6):
        draw_petal()
        painter.right(60)

    # Draw stem for the rose
    draw_stem(painter, x, y - 150)

def draw_sunflower(painter, x, y):
    # Draw stem for the sunflower
    draw_stem(painter, x, y - 150)

    painter.penup()
    painter.shape("circle")
    painter.turtlesize(2)
    painter.color("yellow")
    painter.goto(x, y)
    painter.pendown()

    for petal in range(18):
        painter.right(20)
        painter.forward(30)
        painter.stamp()

    painter.penup()
    painter.goto(x, y - 30)
    painter.color("brown")
    painter.pendown()
    for petal in range(12):
        painter.right(30)
        painter.forward(30)
        painter.stamp()

def draw_lily(painter, x, y):
    painter.penup()
    painter.goto(x, y)
    painter.pendown()
    painter.color("green")
    painter.pensize(5)

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
    
    # Draw stem for the lily
    draw_stem(painter, x, y - 150)

def draw_violet(painter, x, y):
    painter.penup()
    painter.goto(x, y)
    painter.pendown()
    painter.color("purple")
    painter.pensize(3)

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

    # Draw stem for the violet
    draw_stem(painter, x, y - 150)

# Get user input
userinput = input("I draw flowers. What flower and how many would you like me to draw? ").strip()
flower_choice = userinput.split()
flower_type = None
num = 0

# Process user input
for word in flower_choice:
    if word.isdigit():
        num = int(word)
        if num > 30:
            print("Our max on one run is 30")
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
    x_offset, y_offset = 150, -150
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

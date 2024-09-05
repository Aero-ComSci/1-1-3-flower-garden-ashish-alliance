import turtle as trtl

def draw_tulip(painter, x, y):
    # Draw the petals
    painter.penup()
    painter.shape("circle")
    painter.turtlesize(2)
    painter.goto(x, y)
    painter.setheading(0)
    
    painter.color("darkorchid")
    painter.pendown()
    draw_petal(painter, "darkorchid", 18, 30)
    painter.penup()
    painter.goto(x, y - 30)
    draw_petal(painter, "blue", 12, 30)
    
    # Draw the stem
    painter.color("green")
    painter.pensize(15)
    painter.goto(x, y - 300)
    painter.setheading(90)  # Point upwards
    painter.pendown()
    painter.forward(150)
    painter.setheading(180)
    painter.circle(20, 180)  # Curve at the bottom
    painter.setheading(0)  # Reset heading
    painter.penup()

def draw_sunflower(painter, x, y):
    # Draw the petals
    painter.penup()
    painter.shape("circle")
    painter.turtlesize(2)
    painter.goto(x, y)
    painter.setheading(0)
    
    painter.color("yellow")
    painter.pendown()
    draw_petal(painter, "yellow", 18, 30)
    painter.penup()
    painter.goto(x, y - 30)
    draw_petal(painter, "brown", 12, 30)
    
    # Draw the stem
    painter.color("green")
    painter.pensize(15)
    painter.goto(x, y - 300)
    painter.setheading(90)  # Point upwards
    painter.pendown()
    painter.forward(150)
    painter.setheading(180)
    painter.circle(20, 180)  # Curve at the bottom
    painter.setheading(0)  # Reset heading
    painter.penup()

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

    # Draw the stem
    painter.color("green")
    painter.pensize(7)
    painter.penup()
    painter.goto(x, y - 100)
    painter.setheading(90)  # Point upwards
    painter.pendown()
    painter.forward(100)
    painter.setheading(180)
    painter.circle(15, 180)  # Curve at the bottom
    painter.setheading(0)  # Reset heading
    painter.penup()

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
    
    # Draw the stem
    painter.color("green")
    painter.pensize(7)
    painter.penup()
    painter.goto(x, y - 150)
    painter.setheading(90)  # Point upwards
    painter.pendown()
    painter.forward(150)
    painter.setheading(180)
    painter.circle(20, 180)  # Curve at the bottom
    painter.setheading(0)  # Reset heading
    painter.penup()

def draw_petal(painter, petal_color, petal_count, petal_size):
    painter.color(petal_color)
    painter.pendown()
    for _ in range(petal_count):
        painter.forward(petal_size)
        painter.stamp()
        painter.right(360 / petal_count)
    painter.penup()

def get_user_input():
    valid_flowers = ["roses", "tulips", "violets", "lilies", "sunflowers"]
    
    while True:
        # Prompt the user for input
        user_input = input("I draw flowers. What flower and how many would you like me to draw? (e.g., 3 tulips): ").strip().lower()
        flower_type = None
        num = 1  # Default to 1 if no number is provided

        # Split the input and process each part
        parts = user_input.split()
        for part in parts:
            if part.isdigit():
                num = int(part)
                if num > 30:
                    print("Our max on one run is 30. Limiting to 30.")
                    num = 30
                break

        if num == 0:
            num = 1  # Ensure at least 1 flower if no number is given

        # Determine flower type
        for part in parts:
            if part in valid_flowers:
                flower_type = part
                break

        # Validate and return if input is correct
        if flower_type in valid_flowers and num > 0:
            return flower_type, num
        else:
            print("Invalid input. Please enter a valid flower type from: roses, tulips, violets, lilies, sunflowers, and a valid number of flowers (1-30).")

# Get user input
flower_type, num = get_user_input()

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

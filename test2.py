import turtle as trtl

# Function to draw a tulip
def draw_tulip(painter):
    # Stem
    painter.color("green")
    painter.pensize(15)
    painter.goto(0, -150)
    painter.setheading(90)
    painter.forward(100)
    # Leaf
    painter.setheading(270)
    painter.circle(20, 120, 20)
    painter.setheading(90)
    painter.goto(0, -60)
    # Rest of stem
    painter.forward(60)
    painter.setheading(0)

    # Draw flower
    painter.penup()
    painter.shape("circle")
    painter.turtlesize(2)
    painter.color("darkorchid")
    painter.goto(20, 190)

    for petal in range(18):
        painter.right(20)
        painter.forward(30)
        painter.stamp()

    # Ring 2 of flower
    painter.goto(20, 160)
    painter.color("blue")

    for petal in range(12):
        painter.right(30)
        painter.forward(30)
        painter.stamp()

# Function to draw a rose
def draw_rose(painter):
    painter.color("red")
    painter.pensize(3)

    def draw_petal():
        painter.circle(50, 60)
        painter.left(120)
        painter.circle(50, 60)
        painter.left(120)

    # Draw petals
    for _ in range(6):
        draw_petal()
        painter.right(60)

    # Draw stem
    painter.color("green")
    painter.pensize(3)
    painter.goto(0, -150)
    painter.setheading(90)
    painter.forward(100)
    painter.setheading(270)
    painter.circle(20, 120, 20)
    painter.setheading(90)
    painter.goto(0, -60)
    painter.forward(60)
    painter.setheading(0)

# Function to draw a sunflower
def draw_sunflower(painter):
    # Draw stem
    painter.color("green")
    painter.pensize(15)
    painter.goto(0, -150)
    painter.setheading(90)
    painter.forward(100)
    painter.setheading(270)
    painter.circle(20, 120, 20)
    painter.setheading(90)
    painter.goto(0, -60)
    painter.forward(60)
    painter.setheading(0)

    # Draw flower
    painter.penup()
    painter.shape("circle")
    painter.turtlesize(2)
    painter.color("yellow")
    painter.goto(20, 190)

    for petal in range(18):
        painter.right(20)
        painter.forward(30)
        painter.stamp()

    # Ring 2 of flower
    painter.goto(20, 160)
    painter.color("brown")

    for petal in range(12):
        painter.right(30)
        painter.forward(30)
        painter.stamp()

# Function to draw a lily
def draw_lily(painter):
    painter.color("green")
    painter.pensize(5)

    def draw_petal():
        painter.circle(50, 60)
        painter.left(120)
        painter.circle(50, 60)
        painter.left(120)

    # Draw petals
    for _ in range(6):
        painter.begin_fill()
        draw_petal()
        painter.end_fill()
        painter.right(60)

# Function to draw a violet
def draw_violet(painter):
    painter.color("purple")
    painter.pensize(3)

    def draw_petal():
        painter.circle(50, 60)
        painter.left(120)
        painter.circle(50, 60)
        painter.left(120)

    # Draw petals
    for _ in range(6):
        painter.begin_fill()
        draw_petal()
        painter.end_fill()
        painter.right(60)

    # Draw stem
    painter.color("green")
    painter.pensize(3)
    painter.goto(0, -150)
    painter.setheading(90)
    painter.forward(100)

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
    for _ in range(num):
        if flower_type == "tulips":
            draw_tulip(painter)
        elif flower_type == "roses":
            draw_rose(painter)
        elif flower_type == "sunflower":
            draw_sunflower(painter)
        elif flower_type == "lilies":
            draw_lily(painter)
        elif flower_type == "violets":
            draw_violet(painter)

    # Hide turtle and finish
    painter.hideturtle()
    screen.mainloop()

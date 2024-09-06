import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle named "painter"
painter = turtle.Turtle()
painter.speed(2000)  # Adjust speed to your liking
painter.color("purple")
painter.pensize(3)  # Make the pen thicker for the petals

# Function to draw a petal
def draw_petal():
    painter.circle(50, 60)  # Draw an arc with radius 50 and 60 degrees
    painter.left(120)
    painter.circle(50, 60)
    painter.left(120)

# Draw the painter petals
for _ in range(6):
    painter.begin_fill()
    draw_petal()
    painter.end_fill()
    painter.right(60)

painter.color("green")
painter.pensize(3)
painter.goto(0, -150)
painter.setheading(90)
painter.forward(100)

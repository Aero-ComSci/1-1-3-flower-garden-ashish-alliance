import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("blue")

# Create a turtle named "painter"
painter = turtle.Turtle()
painter.speed(2000)  # Adjust speed to your liking
painter.color("green")
painter.pensize(5)  # Make the pen thicker for the petals

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


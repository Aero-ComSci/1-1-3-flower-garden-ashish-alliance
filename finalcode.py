import turtle as trtl

def draw_petal(painter, petal_color, petal_count, petal_size):
    painter.color(petal_color)
    painter.pendown()
    for _ in range(petal_count):
        painter.forward(petal_size)
        painter.stamp()
        painter.right(360 / petal_count)
    painter.penup()

def draw_tulip(painter, x, y):
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
    
    painter.color("green")
    painter.pensize(15)
    painter.goto(x, y - 300)
    painter.setheading(90)
    painter.pendown()
    painter.forward(150)
    painter.setheading(180)
    painter.circle(20, 180)
    painter.setheading(0)
    painter.penup()

def draw_sunflower(painter, x, y):
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
    
    painter.color("green")
    painter.pensize(15)
    painter.goto(x, y - 300)
    painter.setheading(90)
    painter.pendown()
    painter.forward(150)
    painter.setheading(180)
    painter.circle(20, 180)
    painter.setheading(0)
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

    painter.color("green")
    painter.pensize(7)
    painter.penup()
    painter.goto(x, y - 100)
    painter.setheading(90)
    painter.pendown()
    painter.forward(100)
    painter.setheading(180)
    painter.circle(15, 180)
    painter.setheading(0)
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
    
    painter.color("green")
    painter.pensize(7)
    painter.penup()
    painter.goto(x, y - 150)
    painter.setheading(90)
    painter.pendown()
    painter.forward(150)
    painter.setheading(180)
    painter.circle(20, 180)
    painter.setheading(0)
    painter.penup()

def get_user_input():
    valid_flowers = {"roses": draw_rose, "tulips": draw_tulip, "violets": draw_violet, "lilies": draw_lily, "sunflowers": draw_sunflower}
    
    while True:
        user_input = input("I draw flowers. What flower and how many would you like me to draw? (e.g., 3 tulips): ").strip().lower()
        parts = user_input.split()
        
        num = 1
        flower_type = None
        last_num = None
        
        for part in parts:
            if part.isdigit():
                last_num = int(part)
            elif part in valid_flowers:
                flower_type = part
        
        if flower_type:
            num = last_num if last_num is not None else num
            num = min(num, 30)  # Limit to 30

            if num > 0:
                return flower_type, num
            else:
                print("Invalid number. Please enter a valid number (1-30).")
        else:
            print("Invalid input. Please enter a valid flower type (roses, tulips, violets, lilies, sunflowers) and a valid number (1-30).")

flower_type, num = get_user_input()

screen = trtl.Screen()
screen.bgcolor("white")
painter = trtl.Turtle()
painter.speed(0)

x_start, y_start = -200, 200
x_offset, y_offset = 100, -100
flower_func = {
    "tulips": draw_tulip,
    "roses": draw_rose,
    "sunflowers": draw_sunflower,
    "lilies": draw_lily,
    "violets": draw_violet
}

for i in range(num):
    position_x = x_start + i * x_offset
    position_y = y_start + i * y_offset
    flower_func[flower_type](painter, position_x, position_y)

painter.hideturtle()
screen.mainloop()

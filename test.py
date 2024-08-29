import turtle
from collections import defaultdict

class Flower:
    def __init__(self, flower_type, num_flowers, num_petals):
        self.flower_type = flower_type
        self.num_flowers = num_flowers
        self.num_petals = num_petals

    def draw_flower(self, turtle_obj):
        flower_colors = {
            'rose': 'red',
            'tulip': 'orange',
            'daisy': 'white',
            'sunflower': 'yellow',
            'lily': 'purple'
        }
        turtle.color()
        
        for _ in range(self.num_petals):
            turtle_obj.forward(50)
            turtle_obj.left(360 / self.num_petals)
            turtle_obj.forward(50)
            turtle_obj.left(360 / self.num_petals)
        turtle_obj.right(360 / self.num_flowers)

    def draw(self, turtle_obj):
        turtle_obj.penup()
        for _ in range(self.num_flowers):
            self.draw_flower(turtle_obj)
            turtle_obj.penup()
            turtle_obj.forward(150)
            turtle_obj.pendown()

# Tokenize input and identify flowers and quantities
def parse_input(user_input):
    # Lowercase and split input into words
    words = user_input.lower().split()
    flower_types = {'rose', 'tulip', 'daisy', 'sunflower', 'lily'}
    flower_counts = defaultdict(int)
    petal_counts = defaultdict(int)
    
    i = 0
    while i < len(words):
        if words[i].isdigit():
            quantity = int(words[i])
            if i + 1 < len(words) and words[i + 1] == 'petals':
                if last_flower_type:
                    petal_counts[last_flower_type] = quantity
                i += 2  # Skip 'petals'
            else:
                if last_flower_type:
                    flower_counts[last_flower_type] = quantity
                i += 1
        elif words[i] in flower_types:
            last_flower_type = words[i]
            i += 1
        else:
            i += 1  # Skip unrecognized words
    
    return flower_counts, petal_counts

# Main function to draw flowers based on user input
def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    
    user_input = input("Enter flower types and quantities (e.g., 3 roses, 2 tulips with 6 petals): ")
    flower_counts, petal_counts = parse_input(user_input)

    turtle_obj = turtle.Turtle()
    turtle_obj.speed(1)
    
    for flower_type, count in flower_counts.items():
        petals = petal_counts.get(flower_type, 5)  # Default petals to 5 if not specified
        flower = Flower(flower_type, count, petals)
        flower.draw(turtle_obj)
    
    screen.mainloop()

if __name__ == "__main__":
    main()

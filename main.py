from canvas import Canvas
from shapes import Rectangle, Square


# Get the width and the height of the canvas from the user
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color codes and ask the color choice for the user
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color(white or black): ")

# Create a canvas from the user data
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type = input("What do you like to draw? Enter quit to quit. ")
    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter the x coordinate of the rectangle: "))
        rec_y = int(input("Enter the y coordinate of the rectangle: "))
        rec_width = int(input("Enter the width of the rectangle: "))
        rec_height = int(input("Enter the height of the rectangle: "))
        red = int(input("How much red should the rectangle have: "))
        green = int(input("How much green should the rectangle have: "))
        blue = int(input("How much blue should the rectangle have: "))

        # Create the rectangle
        r1 = Rectangle(
            x=rec_x,
            y=rec_y,
            height=rec_height,
            width=rec_width,
            color=(red, green, blue),
        )
        r1.draw(canvas)
    if shape_type.lower() == "square":
        square_x = int(input("Enter the x coordinate of the square: "))
        square_y = int(input("Enter the y coordinate of the square: "))
        square_side = int(input("Enter the side length of the square: "))
        red = int(input("How much red should the square have: "))
        green = int(input("How much green should the square have: "))
        blue = int(input("How much blue should the square have: "))
        s1 = Square(x=square_x, y=square_y, side=square_side, color=(red, green, blue))
        s1.draw(canvas)
    if shape_type.lower().strip() == "quit":
        break

canvas.make("canvas.png")

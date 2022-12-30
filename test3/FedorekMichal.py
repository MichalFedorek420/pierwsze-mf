import time
import turtle
from math import cos, pi, radians, sin
from random import randint


def draw_square(x, y, rotation, line_color, fill_color, size, line_width):
    """Draws the square."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.width(line_width)
    turtle.right(rotation)
    turtle.color(line_color, fill_color)
    turtle.begin_fill()
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.end_fill()


def draw_triangle(x, y, rotation, line_color, fill_color, size, line_width):
    """Draws the triangle."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.width(line_width)
    turtle.right(rotation)
    turtle.color(line_color, fill_color)
    turtle.begin_fill()
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.goto(x, y)
    turtle.end_fill()


def draw_octagon(x, y, rotation, line_color, fill_color, size, line_width):
    """Draws the octagon."""
    size = size / 2
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.width(line_width)
    turtle.right(rotation)
    turtle.color(line_color, fill_color)
    turtle.begin_fill()
    while True:
        turtle.forward(size)
        turtle.left(45)
        if abs(turtle.Vec2D(x, y) - turtle.pos()) < 1:
            break
    turtle.end_fill()


def draw_devilstar(x, y, rotation, line_color, fill_color, size, line_width):
    """Draws the devilstar."""
    size = size / 1.5
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.width(line_width)
    turtle.right(rotation)
    turtle.color(line_color, fill_color)
    angle = 150
    arms = 5
    arm_rotation = 360 / arms

    turtle.begin_fill()
    for _ in range(arms):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.left(angle)
        turtle.right(arm_rotation)

    turtle.end_fill()


def draw_rombus(x, y, rotation, line_color, fill_color, size, line_width):
    """Draws the rombus."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.width(line_width)
    turtle.right(rotation)
    turtle.color(line_color, fill_color)
    turtle.begin_fill()
    turtle.forward(size)
    turtle.left(70)
    turtle.forward(size)
    turtle.left(110)
    turtle.forward(size)
    turtle.left(70)
    turtle.forward(size)
    turtle.end_fill()


def get_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b

def get_random_line_width():
    return randint(1, 10)


def giga_circle(x, y, number_of_shapes, radius, size, rotation):
    """Draws giga circle"""

    shapes_functions = [
        draw_square,
        draw_triangle,
        draw_octagon,
        draw_devilstar,
        draw_rombus,
    ]
    angle = 360 // number_of_shapes
    rotation = 0
    turtle_speed = 0
    turtle.speed(turtle_speed)
    for current_angle in range(0, 360, angle):
        turtle_speed += 1
        turtle.speed(turtle_speed)
        current_angle_rad = pi / 2 - radians(current_angle)
        shape_x = x + radius * cos(current_angle_rad)
        shape_y = y + radius * sin(current_angle_rad)
        shapes_functions[int((current_angle / angle) % len(shapes_functions))](
            shape_x, shape_y, rotation, get_random_color(), get_random_color(), size, get_random_line_width()
        )


def sign(x, y, text):
    """Sgining function."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(text, font=("Courier", 24, "bold"))


def main():
    start = time.time()
    turtle.colormode(255)
    turtle.bgcolor(get_random_color())
    giga_circle(0, 0, 100, 300, 50, 0)
    sign(88, 360, "Michał Fedorek ZZISS1-1111")
    finish = time.time() - start
    print(f"Time taken: {finish} s.")
    turtle.done()


if __name__ == "__main__":
    main()

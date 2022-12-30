import turtle
from math import pi, radians, sin, cos
from turtle import begin_fill, color, end_fill, forward, left, goto, right, penup, pendown


def draw_square(x, y, rotation, line_color, fill_color, size):
    """Draws the square."""
    penup()
    goto(x,y)
    pendown()
    right(rotation)
    color(line_color, fill_color)
    begin_fill()
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    end_fill()


def draw_triangle(x, y, rotation, line_color, fill_color, size):
    """Draws the triangle."""
    penup()
    goto(x,y)
    pendown()
    right(rotation)
    color(line_color, fill_color)
    begin_fill()
    forward(size)
    left(90)
    forward(size)
    goto(x,y)
    end_fill()


def draw_octagon(x, y, rotation, line_color, fill_color, size):
    """Draws the octagon."""
    penup()
    goto(x,y)
    pendown()
    right(rotation)
    color(line_color, fill_color)
    begin_fill()
    while True:
        forward(size)
        left(45)
        if abs(turtle.Vec2D(x, y)-turtle.pos())<1:
            break
    end_fill()


def draw_devilstar(x, y, rotation, line_color, fill_color, size):
    """Draws the devilstar."""
    penup()
    goto(x,y)
    pendown()
    right(rotation)
    color(line_color, fill_color)
    angle=150
    arms = 5
    arm_rotation = 360/arms

    begin_fill()
    for _ in range(arms):

        forward(size)
        right(angle)
        forward(size)
        left(angle)
        right(arm_rotation)

    end_fill()


def draw_rombus(x, y, rotation, line_color, fill_color, size):
    """Draws the rombus."""
    penup()
    goto(x,y)
    pendown()
    right(rotation)
    color(line_color, fill_color)
    begin_fill()
    forward(size)
    left(70)
    forward(size)
    left(110)
    forward(size)
    left(70)
    forward(size)
    end_fill()


def giga_circle(x, y, number_of_shapes,radius, size, rotation):
    """Draws giga circle"""
    shapes_functions = [draw_square, draw_triangle, draw_octagon, draw_devilstar, draw_rombus]
    # goto(x,y)
    angle=360//number_of_shapes
    rotation=0
    line_color = "red"
    fill_color = "yellow"
    for current_angle in range(0, 360, angle):
        current_angle_rad = pi/2 - radians(current_angle)
        shape_x = x + radius * cos(current_angle_rad)
        shape_y = y + radius * sin(current_angle_rad)
        shapes_functions[int((current_angle/angle) % len(shapes_functions))](
            shape_x,
            shape_y,
            rotation,
            line_color,
            fill_color,
            size)
    # goto(angle,radius)
    # draw_square()

    
def main():
    # draw_square(100,100,90,"blue","green",100)
    # draw_triangle(150,150,90,"green","blue",200)
    # draw_octagon(200,200,90,"pink","brown",150)
    # draw_devilstar(230,230,90,"black","yellow",100)
    # draw_rombus(100,100,45,"grey","red",135)
    giga_circle(0, 0, 20, 300, 50, 0)
    turtle.done()


if __name__ == "__main__":
    main()
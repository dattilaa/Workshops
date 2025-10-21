import turtle as trt
import math

trt.tracer(0)
trt.pencolor('white')


def rotate_point(p, angle, center) -> tuple:
    rad = math.radians(angle)
    x, y = p
    cx, cy = center
    xr = cx + (x - cx) * math.cos(rad) - (y - cy) * math.sin(rad)
    yr = cy + (x - cx) * math.sin(rad) + (y - cy) * math.cos(rad)
    return xr, yr


def triangle(x, y, z, color):
    trt.penup()
    trt.goto(x)
    trt.pendown()
    trt.fillcolor(color)
    trt.begin_fill()
    trt.goto(y)
    trt.goto(z)
    trt.goto(x)
    trt.end_fill()
    trt.penup()


def square(l, x, y, color1, color2, rotation):
    cx = x + l / 2
    cy = y + l / 2

    p1 = (x, y)
    p2 = (x + l, y)
    p3 = (x + l, y + l)
    p4 = (x, y + l)

    p1 = rotate_point(p1, rotation, (cx, cy))
    p2 = rotate_point(p2, rotation, (cx, cy))
    p3 = rotate_point(p3, rotation, (cx, cy))
    p4 = rotate_point(p4, rotation, (cx, cy))

    triangle(p1, p2, p4, color1)
    triangle(p3, p4, p2, color2)


def bigger_square(x, y, angle):
    center = (x + 75, y - 75)

    positions = [
        (0, 0, 'bisque3', 'bisque4'),
        (0, -50, 'AntiqueWhite2', 'bisque3'),
        (0, -100, 'bisque3', 'AntiqueWhite2'),
        (50, 0, 'bisque4', 'bisque3'),
        (100, 0, 'bisque3', 'AntiqueWhite2'),
        (50, -50, 'bisque3', 'bisque4'),
        (50, -100, 'AntiqueWhite2', 'bisque3'),
        (100, -50, 'bisque4', 'bisque3'),
        (100, -100, 'bisque3', 'bisque4'),
    ]

    for dx, dy, c1, c2 in positions:
        px, py = x + dx, y + dy
        rx, ry = rotate_point((px, py), angle, center)
        square(50, rx, ry, c1, c2, angle)


bigger_square(0, 0, 0)
bigger_square(150, 50, 90)
bigger_square(-50, -150, -90)
bigger_square(100, -100, 180)






from math import pi
default_radius = 5
def circle_perimeter(radius=default_radius):
    p = pi * 2 * radius
    print(p)
def circle_area(radius=default_radius):
    s = pi * radius ** 2
    print(s)
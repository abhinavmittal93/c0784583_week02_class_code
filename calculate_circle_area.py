import math


def calc_radius():
    radius = float(input('Enter the radius of the circle: '))
    area = math.pi * radius ** 2
    return f'Area of the circle is: {area:.2f}'

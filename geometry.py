# This program contains functions that evaluate formulas used in geometry.
#
# Your Name
# August 22, 2014

import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

def parallelogram_area(b, h):
    a = b * h
    return a

def trapezoid_area(b, c, h):
    a = ((b + c) / 2) * h
    return a

def rectangular_prism_volume(w, h, l):
    a = w * h * l
    return a

def cone_volume(r, h):
    a = math.pi * r**2 * (h / 3)
    return a

def sphere_volume(r):
    a = (4 / 3) * math.pi * r**3
    return a

def rectangular_prism_surface_area(w, l, h):
    a = 2 * (w * l + h * l + h * w)
    return a

def sphere_surface_area(r):
    a = 4 * math.pi * r**2
    return a

def triangle_hypotenuse(a, b):
    h = math.sqrt((a**2 + b**2))
    return h

# function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))
print(parallelogram_area(1,2))
print(trapezoid_area(3, 4, 5))
print(rectangular_prism_volume(6, 7, 8))
print(cone_volume(1, 2))
print(sphere_volume(3))
print(rectangular_prism_surface_area(4, 5, 6))
print (sphere_surface_area(7))
print(triangle_hypotenuse(1, 2))

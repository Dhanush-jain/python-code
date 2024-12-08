import math

# Function to calculate the area and perimeter of a circle
def circle(radius):
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area, perimeter

# Function to calculate the area and perimeter of a triangle
def triangle(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    perimeter = a + b + c
    return area, perimeter

# Function to calculate the area and perimeter of a square
def square(side):
    area = side ** 2
    perimeter = 4 * side
    return area, perimeter

# Example usage
circle_area, circle_perimeter = circle(5)
triangle_area, triangle_perimeter = triangle(3, 4, 5)
square_area, square_perimeter = square(4)

# Print results
print("Circle - Area:", circle_area, "Perimeter:", circle_perimeter)
print("Triangle - Area:", triangle_area, "Perimeter:", triangle_perimeter)
print("Square - Area:", square_area, "Perimeter:", square_perimeter)

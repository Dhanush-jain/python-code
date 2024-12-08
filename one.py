import math
import cmath

def find_roots(a, b, c):
    if a == 0:
        if b != 0:
            print("This is a linear equation. Root:", -c / b)
        else:
            print("Invalid equation. Coefficients a and b cannot both be zero.")
        return
    
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Roots are real and distinct:")
        print("Root 1 =", root1)
        print("Root 2 =", root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        print("Roots are real and identical:")
        print("Root =", root)
    else:
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        print("Roots are complex:")
        print("Root 1 =", root1)
        print("Root 2 =", root2)

# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

find_roots(a, b, c)

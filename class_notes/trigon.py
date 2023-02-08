# Do any necessary imports here
import math

# Complete the function
def circle_area(r):
    return r*r * math.pi


inp = float(input("Enter the radius of a circle:"))
print("Area of circle =", circle_area(inp))

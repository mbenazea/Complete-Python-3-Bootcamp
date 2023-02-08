import math

#area of a circle
def area_cirle(radius, pi=math.pi):
    """
    This a function that compute the area of a circle
    params:
        radius: the radius of the circle
        pi: this is a constant, with value 3.14
        
    """
    result = pi * radius **2
    return result
    print(area_cirle(4, pi=
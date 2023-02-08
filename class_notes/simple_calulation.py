
import math
#area of a reactangle 
def area_retangle (length, width):
    #fxn that return the arae of a rectangle
    return (length * width)


#area of a cirle 
def area_circle(radius, pi= math.pi):                     

    result = pi * radius**2
    return result

# area of triangle
def area_triangle( height , base):

    result = base/2 * height
    return result

# prevent this code from running when this file is imported
# but code can rune when this file is executed.    
if __name__=="__main__":
    print("Rectangle area" , area_retangle(10, 5)) 
    print ("cirle area:", area_circle(10))
    print("Traingel area:", area_triangle(10, 4))
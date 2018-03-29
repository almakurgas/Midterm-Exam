"""
===================   TASK 1   ====================
* Name: Area Of Circle
*
* Write a function `area_of_circle` that will
* return area enclosed by a circle of radius `r`.
* Consider that only float value for radius will
* be passed. Negative values should be considered
* as typo and function should ignore sign of a
* number.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================

"""
def area_of_circle(radius):
    """
    Calculates cube volume for given side.
    Returns -1 if argument is not int or float
    """
    if (not isinstance(radius, int)) and (not isinstance(radius, float)):
        return -1





    import math
    return math.pi * radius **2

radius  = 5.0
circle = area_of_circle(radius)
print("Area of circle is: ", circle)






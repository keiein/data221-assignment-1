#assignment_question_5.py
#Define a function with 2 arguments containing radii of 2 circles
#Compute the area, and the percentage of the larger circle's area that the smaller circle covers
#Make sure that both radii are positive, if not then print a message

from math import pi #import pi from math

def circle_area_coverage(radius_of_circle_1:int, radius_of_circle_2:int) -> str: #Given function definition
    if radius_of_circle_1 > 0 and radius_of_circle_2 > 0: #Checks if both radii are positive, if it is then run the following block
        area_of_circle_1 = radius_of_circle_1 * radius_of_circle_1*pi #calculates r^2*pi for both radii
        area_of_circle_2 = radius_of_circle_2 * radius_of_circle_2*pi
        if area_of_circle_1 > area_of_circle_2: #checks if the first circle is bigger than the second, then vice versa
            percent = (area_of_circle_2/area_of_circle_1)*100 #calculates the percentage
        else:
            percent = (area_of_circle_1/area_of_circle_2)*100
        return str(percent) + "% of the larger circle's area can be covered by the smaller circle." #returns the percentage
    else: #if at least one of the radii is negative
        return 'At least one of the radius is negative.' #returns a meaningful text


#assignment_question_4.py
#Given a list of values and a value x, sort the list, find the first index where the value in the list is greater than or equal to x

#Starter code
from random import random

values = [random() for i in range(20)]
x = random()

#End of starter code

values.sort() #sort the list of values

matching_index = -1 #a default index value (matching index is not found yet)

for index in range(len(values)): #variable index from 0 to the values list length
    if values[index] >= x: #if the value in the list at that index is greater or equal to x
        matching_index = index #set the matching index to that index
        break #end the loop right away (to get the FIRST matching index)

#print statements
print("Sorted list: " + str(values))
print("The value of x: " + str(x))


if matching_index == -1: #if matching index doesn't exist
    print("No matching index.")
else: #otherwise
    print("Matching index: " + str(matching_index))
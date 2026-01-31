#assignment_question_1.py
#Controlled Multiplication Loop
#A program that multiplies consecutive integers from 1 until the product becomes greater than a given threshold

threshold_value_to_stop_loop = 120 #Stores the threshold value
product_of_numbers = 1 #Stores the product
incrementing_number = 1 #The number multiplying with the product

while product_of_numbers <= threshold_value_to_stop_loop: #This block runs as long as product is less than or equal to the threshold
    incrementing_number += 1 #Number increments
    product_of_numbers *= incrementing_number #Multiplies that number to the product of numbers


print("The final product is: " + str(product_of_numbers) + " and the integer causing the product to go over the threshold is: " + str(incrementing_number))


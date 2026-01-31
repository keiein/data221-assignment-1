#assignment_question_3.py
#Define a function that computes x^y, given a list of pairs (x,y), return the computation in another list
#Skips the pair if y is negative

def exponent_computer(list_of_pairs:list[list[int]]) -> list[int]: #Defines function exponent_computer that takes a list of pairs, returns list
    list_of_results = [] #An empty list that stores the results x^y
    for list_of_pair in list_of_pairs: #Iterate through each pair in the list
        if list_of_pair[1] >= 0: #If the exponent part, second value, is greater than or equal to 0
            list_of_results.append(list_of_pair[0]**list_of_pair[1]) #Compute x^y and add it to the list of results

    return list_of_results #return the final list



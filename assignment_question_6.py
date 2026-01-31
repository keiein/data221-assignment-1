#assignment_question_6.py
#Define a function that receives a list of numbers and returns a dictionary

def distribution_analysis(list_of_numbers:list[int]) -> dict[int, float]: #Defining function taking in a list of ints returns dictionary, key int, value float
    list_of_numbers.sort() #Sort the keys
    dictionary_of_percentages = {}
    for i in range(len(list_of_numbers)): #iterate using indices
        dictionary_of_percentages[list_of_numbers[i]] = (i+1)/len(list_of_numbers)*100 #for each number in the list, have a key with its value as the percentage of elements less than or equal to that
    return dictionary_of_percentages #return it

#print(distribution_analysis([3,1,2,3,4,2]))



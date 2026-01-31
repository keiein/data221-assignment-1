#assignment_question_2.py
#Define a function that receives a list of strings and returns a dictionary consisting of string length and parity of that length

def length_parity_dictionary(list_of_strings:list[str]) -> dict[str, dict]: #Takes in list_of_strings and type-hint dictionary
    length_parity = {}
    for string in list_of_strings: #Iterate through all strings in the list
        length_parity[string] = {
            "length":len(string),
            "parity":"even" if len(string) % 2 == 0 else "odd"
        } #Add the key-value pair, value being another dictionary

    return length_parity #return the final dictionary

p


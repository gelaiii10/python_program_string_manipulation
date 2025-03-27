def custom_lstrip(input_string):
    #initialize an index to track the position of the first non-space character
    index = 0 
    while index < len(input_string) and input_string[index] == ' ': #loop through the string until we find a non space character
        index += 1
    #return the substring starting from the first non-space character
    return input_string[index:]

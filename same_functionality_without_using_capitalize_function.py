#input string
input_string = "hELLO wORLD"
#check if the string is empty
if not input_string:
    result = input_string
else:
    #capitalize the first character and make the rest lowercase
    first_char = input_string[0].upper()  #capitalize the first character
    rest_of_string = input_string[1:].lower()  #convert the rest to lowercase

    result = first_char + rest_of_string #integrate the results

print(result) #print the result  
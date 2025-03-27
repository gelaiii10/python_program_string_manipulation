input_string = "hello, world! this is just a test."  #original string
result = ""
capitalize_next = True  #flag to indicate if the next character should be capitalized

for i in input_string:
    if i == ' ':
        result += i  #keep spaces as they are
        capitalize_next = True  #next character should be capitalized
    elif capitalize_next:
        result += i.upper()  #capitalize the character
        capitalize_next = False  #reset the flag
    else:
        result += i.lower()  #make the character lowercase
#print the result
print(input_string)
print(result)        
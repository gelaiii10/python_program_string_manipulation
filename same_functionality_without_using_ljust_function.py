#original string
input_string = "Hello"
#desired total width
width = 10  
#compute the number of spaces needed
spaces_needed = width - len(input_string)
#if the input string is already longer than the specified width return it as is
if spaces_needed <= 0:
    result = input_string
else:
    #add spaces to the end of the string
    result = input_string + ' ' * spaces_needed
#print the output result
print(input_string)
print(result)
print({len(result)})     

#input string and desired width
string = "HELLO"
width = 10
#calculate the number of spaces needed
spaces_needed = width - len(string)
#if spaces_needed is less than or equal to 0, use the original string
if spaces_needed <= 0:
    result = string
else:
    #create a string of spaces and connect it with the original string
    result = ' ' * spaces_needed + string
#print the output
print(string)
print(result)
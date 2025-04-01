#input string and desired width
string = "42"
width = 5
#calculate the number of zeros needed
zeros_needed = width - len(string)
#if zeros_needed is less than or equal to 0 use the original string
if zeros_needed <= 0:
    result = string
else:
    #create a string of zeros and connect it with the original string
    result = '0' * zeros_needed + string
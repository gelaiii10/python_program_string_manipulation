#input a string
input_string = "HELLO WORLD!"  #change this to test with different strings
all_upper = True  #assume the string is all uppercase initially

for i in input_string:
    #check if the character is not an uppercase letter
    if not ('A' <= i <= 'Z'):
        all_upper = False  #found a non-uppercase character
        break  #break the code
#condition to print the result
if all_upper: 
    print(input_string)
else:
    print(input_string)
input_string = "Hello"  #original string
width = 15              #desired total width
#compute the total number of spaces needed
spaces_needed = width - len(input_string)

if spaces_needed <= 0: #if the input string is already longer than the specified width, return it as is
    result = input_string
else:
    #calculate the number of spaces to add on each side
    left_spaces = spaces_needed // 2
    right_spaces = spaces_needed - left_spaces  #ensure total spaces are correct

    #add the centered string
    result = ' ' * left_spaces + input_string + ' ' * right_spaces
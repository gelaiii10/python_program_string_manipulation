def custom_removeprefix(input_string, prefix):
    #if the input string starts with the prefix, return the string without the prefix
    if input_string.startswith(prefix):
        return input_string[len(prefix):]
    return input_string  #return the original string

input_str = "Hello, World!" 
prefix = "Hello, "
result = custom_removeprefix(input_str, prefix)
print(result) #print the result
#input string and suffix to remove
input_string = "hello world!!!"
suffix = "!!"
#check if the input string ends with the specified suffix
if input_string.endswith(suffix):
    new_length = len(input_string) - len(suffix) #calculate the new length of the string without the suffix
    #slit the string to remove the suffix
    result = input_string[:new_length]
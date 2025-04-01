#input string
input_string = "hello, world     " #this is just example of string
index = len(input_string) - 1  #start from the end of the string and find the last non space character

while index >= 0 and input_string[index].isspace():
    index -= 1
#get the substring from the start to the last non space character
result = input_string[:index + 1]
#print the result
print(input_string)
print(result)
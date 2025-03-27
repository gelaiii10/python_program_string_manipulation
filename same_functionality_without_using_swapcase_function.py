input_string = "Hello, World!"  #original string
result = ""

for i in input_string:
    #check if the character is uppercase
    if 'A' <= i <= 'Z':
        #convert to lowercase by adding 32
        result += chr(ord(i) + 32)
    #check if the character is lowercase
    elif 'a' <= i <= 'z':
        #convert to uppercase by subtracting 32
        result += chr(ord(i) - 32)
    else:
        result += i
#print the output result
print(input_string)
print(result)
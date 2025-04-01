#input string
input_string = "hello world!"
result = "" #initialize an empty string to store the result
#repeat through each character in the input string
for i in input_string:
    if 'a' <= i <= 'z': #check if the character is a lowercaze letter
        result += chr(ord(i) - 32) #convert to uppercase by subtracting
else:
    result += i   
#print the result
print(input_string)
print(result)     
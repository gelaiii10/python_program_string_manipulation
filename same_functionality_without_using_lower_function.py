#input a string
input_string = "Hello, World!"
result = ""

for i in input_string:
    #check if the character is an uppercase letter
    if 'A' <= i <= 'Z':
        result += chr(ord(i) + 32) #convert to lowercase 
    else:
        #if it's not an uppercase letter keep it as is
        result += i
#print the result
print(input_string)
print(result)
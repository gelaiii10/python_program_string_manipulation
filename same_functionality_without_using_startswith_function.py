#input string and prefix
string = "HELLO WORLD"
prefix = "HELLO"
#check if the prefix is longer than the string
if len(prefix) > len(string):
    result = False
else:
    result = True #initialize a flag to true
    #compare the beginning of the string with the prefix
    for i in range(len(prefix)):
        if string[i] != prefix[i]:
            result = False
            break
#print the output
if result:
    print(f"the string '{string}' starts with {prefix}")
else:
    print(f"the string '{string}' does not start with {prefix}")
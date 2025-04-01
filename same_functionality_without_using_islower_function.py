#input string
string = "hello world"
#initialize a flag to True
all_lower = True
#check each character in the string
for i in string:
    #if the character is not a lowercase letter
    if not ('a' <= i <= 'z'):
        all_lower = False
        break #break the code
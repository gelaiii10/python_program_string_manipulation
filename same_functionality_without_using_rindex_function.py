#input string and substring to find
string = "hello philippines, hello world"
substring = "hello"
#initialize a variable to store the index
index = -1
substring_length = len(substring)
#for L
# loop through the string in reverse to find the last occurrence of the substring
for i in range(len(string) - substring_length, -1, -1):
    #check if the substring matches the part of the string
    if string[i:i + substring_length] == substring:
        index = i
        break  #exit the loop once the last occurrence is found
#input string and substring to count
string = "hello philippines, hello world"
substring = "hello"
#initialize a counter
count = 0
substring_length = len(substring)
#for loop through the string to find occurrences of the substring
for i in range(len(string) - substring_length + 1):
    #check if the substring matches the part of the string
    if string[i:i + substring_length] == substring:
        count += 1
#print the output
print(f'the substring "{substring}" appears {count} times in the string')
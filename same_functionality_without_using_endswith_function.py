input_string = "Hello, World!"  #string to check
suffix = "World!"                #suffix to check
#check if the length of the suffix is greater than the string
if len(suffix) > len(input_string):
    ends_with_suffix = False
else:
    ends_with_suffix = input_string[-len(suffix):] == suffix #compare the end of the string with the suffix

if ends_with_suffix: #print the result
    print(f"the string '{input_string}' ends with '{suffix}'.")
else:
    print(f"the string '{input_string}' does not end with '{suffix}'.")   
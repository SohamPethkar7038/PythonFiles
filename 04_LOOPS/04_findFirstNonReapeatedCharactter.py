# find the first non repeated character

# in strings we learn about the count inbuild function that it checks about the occurence of the each letter of the string


input_str="sohamsohm"

for char in input_str:
    if input_str.count(char)==1:
        print("non repeated character is : ",char);
        break
    
# break because to stop the loop when we got our non repeated character to be the optimize program
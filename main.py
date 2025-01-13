'''
Name: Amaya Tavernier
Date: 1OCT24
Class/Section: COMP163/004
Description: Upon receiving a string of characters, this program will encode the string 
and return the number of times each character of the same value was used. 
If it surpasses a value of 9, then a new counter for the character will be created (EX. 9A3A). 
'''
unencoded_string = input("What string would you like me to encode?:") # DO NOT CHANGE THIS
encoded = ""  # DO NOT CHANGE THIS
###########  PUT YOUR CODE BELOW THIS LINE  ###########

count = 0
previous_char = None
for c in unencoded_string:
    if previous_char == None:
        previous_char = c
    if c == previous_char and count<9:
        count += 1
    elif c != previous_char: #In order to move on, this branch will add the previous character and its value to the "encoded" string
        encoded += str(count) + previous_char
        previous_char = c
        count = 1
    elif count >= 9: #If the value of a character surpasses 9, this will create a new counter for it
        encoded += str(count) + previous_char
        count = 1
if previous_char != None:
    encoded += str(count) + previous_char
'''
failed :[
unencoded_string_dict = {}
for i in unencoded_string:
    if i in unencoded_string_dict and unencoded_string_dict[i]<9:
        unencoded_string_dict[i] += 1
        #If the key already exists in the dictionary, then this will add 1 to the value
    else:
        unencoded_string_dict[i] = 1
        #If the key does not exist in the dictionary, this will add one and assign it a value of 1
for key,value in unencoded_string_dict.items():
    encoded += str(value) + key
    #Adding the value and key combined to the empty string "encoded"
'''

###########  PUT YOUR CODE ABOVE THIS LINE  ###########
print(f"{unencoded_string} encoded is {encoded}") # DO NOT CHANGE THIS


#Algorithm that checks for "interesting numbers" given 
#a random number. Interesting numbers include increasing 
#and decreasing sequences, numbers consisting of only one digit, 
#numbers with 1 starting digit and the rest zeros, and palindromes.
#We also have to check for the next two numbers after the number
#we're given. To top it off we have to check if the numbers are a 
#part of the "awesome phrases" array that we are given. If the 
#number we are given is "interesting" we return 2, if one of the 
#two numbers after the first is "interesting" we return 1, and if
#none, we return 0. 

#Main function
def is_interesting(number, awesome_phrases):
    #Creates the three numbers we have to check for 
    number_range = [number, number+1, number+2]
    #Create two variables with increasing and decreasing sequences
    sequence, reverse_sequence = '1234567890', '9876543210'
    
    #One edgecase was that the numbers weren't interesting 
    #if they were less than 100, but if the first is less, 
    #then one of the other two can be above.
    if number+2 == 100 or number+2 == 101:
        return 1
    elif number+2<100: return 0
    
    #Loop through the three numbers
    for num in number_range:
        #Check if they are a part of the given array. 
        if num in awesome_phrases:
            #If they are, we check if its the first or the other two
            if num == number_range[0]: return 2
            else: return 1
        #We check if the number is a subsequence of the 
        #sequence variables. 
        if str(num) in sequence:
            if num == number_range[0]: return 2
            else: return 1
        if str(num) in reverse_sequence:
            if num == number_range[0]: return 2
            else: return 1
    #Create a container with all the functions defined below. 
    #This is so we can sort them and retrieve the largest number
    #considering that once function can return 2, and another 
    #can return 1. However, we are only returning the largest value.
    container = [check_divisible(number_range),
                check_palindrome(number_range),
                check_same_digit(number_range)]
    #Reverse sorting to get largest value
    return sorted(container, reverse=True)[0]

#Function that checks for numbers consisting of 
#1 digit and the rest 0's. 
def check_divisible(arr):
    #Loop through the 3 numbers
    for num in arr:
        #Converting to string, to find the length of number. 
        str_num = str(num)
        #Find the rest of dividing. For example: 90000%10000 = 0
        #We also have to divide by same power to not miss numbers
        #like 9300. 
        if num % 10**(len(str_num)-1) == 0:
            if arr.index(num) == 0:
                return 2
            else:
                return 1
    return 0

#Check for same digit. I just check if the string of digits
#is the same as the first digit multiplied by the length. 
def check_same_digit(arr): 
    for num in arr:
        str_num = str(num)
        if str_num == str_num[0]*len(str_num):
            if arr.index(num) == 0: return 2
            else: return 1
    return 0

#Check if the string is the same as the string reversed. 
def check_palindrome(arr):
    for num in arr:
        num_str = str(num)
        if num_str == num_str[::-1]:
            if arr.index(num) == 0: return 2
            else: return 1
    return 0

print(is_interesting(1111111, [333, 1000])==2)
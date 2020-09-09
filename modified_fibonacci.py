#Takes a number, prod, that is potentially a part of 
#the fibonacci sequence. We find the highest possible two
#numbers, that is a part of the sequence, that multiplied
#gives prod. If two numbers multiplied gives prod, then we return 
#the numbers and true. If not we return the highest values thats
#less than prod and false. 
def productFib(prod):
    #Initializes the values of fibonacci
    A = 0
    B = 1
    C = A + B
    
    #Checks the initial numbers, since we change
    #the values in the loop
    if A*B == prod: return [A, B, True]
    #Loop that continues until A*B is equal or greater than prod.
    while A*B <= prod:
        A = B
        B = C
        C = A + B
        if A*B == prod: return [A, B, True]
    return [A, B, False]

print(productFib(1000))
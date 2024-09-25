factors = 0 

for i in range(0, 1001): # iterates through every number between 0 and 1000
    if (i % 3 == 0 or i % 5 == 0): # if i divided by 3 or 5 gives a remainder of 0
        factors += i # add that number to the running count stored in factors 

print(factors) # print the sum of factors 

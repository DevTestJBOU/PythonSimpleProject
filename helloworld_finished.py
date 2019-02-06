#
#Simple Python script to add some numbers 
#
print ("# Julian Burdett")
print ("# Simple noddy Python sum script ") 
print("")

numbers = [2.5, 3, 4, -5]

# start parameter is not provided
numbersSum1 = sum(numbers)
print ("The 1st result is:") 

print(numbersSum1) #result should be 4.5
print("")

print ("# Julian Burdett")
print ("# Simple noddy Python sum script ") 
print("")

numbers = [2.5, 3, 4, -5]

# start parameter is not provided
numbersSum2 = sum(numbers)
# start = 10
numbersSum2 = sum(numbers, 10)#print(numbersSum)

print ("The 2nd result is:")
print (numbersSum2) #result should be 14.5

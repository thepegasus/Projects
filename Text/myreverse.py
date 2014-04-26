#!/usr/bin/python
#Reverse a given string
#Try in-built string manipulation operators
str=raw_input("Enter the string to reverse:");
revstr=str[::-1]
print "Using in built operations: "+revstr

#Use a loop to achieve the same result
reverse=''
for letter in str:
    reverse=letter+reverse
print "Using custom code: "+reverse

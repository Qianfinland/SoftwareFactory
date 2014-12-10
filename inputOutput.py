#!/usr/bin/python
# This program inputs a string from the user and output: 
#length of the string
#number of words in the string
#reverse format of the string
import re

print('Hey, it is nice to see you')
print('Please input some string')
myString = raw_input()
print('Input:' +myString)
length = len(myString)
print('The length of your string is: ' + str(length))
words=len(re.findall(r'\w+',myString))
print('Number of words are: ' +str(words))

print('Reverse format: '+myString[::-1])


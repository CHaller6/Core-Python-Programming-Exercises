#!/usr/bin/env python

print "Please enter five numbers below...\n"
try:
    input1 = raw_input("Enter the first number: ")
    num1 = int(input1)
    input2 = raw_input("Enter the second number: ")
    num2 = int(input2)
    input3 = raw_input("Enter the third number: ")
    num3 = int(input3)
    input4 = raw_input("Enter the fourth number: ")
    num4 = int(input4)
    input5 = raw_input("Enter the fifth number: ")
    num5 = int(input5)
except ValueError, e:
    print "Please enter integers for all five inputs."

ourList = [num1, num2, num3, num4, num5]
ourTuple = (num1, num2, num3, num4, num5)

#Print out the list using a FOR loop
print '\nList output: '
for n in ourList:
    print n,
print '\n'

#Print out the tuple
print '\nTuple output: '
for n in ourTuple:
    print n,
print '\n'

#Print out the list using a WHLIE loop
print '\nList output: '
cur = 0
while cur < len(ourList):
    print ourList[cur],
    cur += 1
print '\n'

#Print out the ruple using a WHILE loop
print '\nTuple output: '
cur = 0
while cur < len(ourTuple):
    print ourTuple[cur],
    cur += 1
print '\n'

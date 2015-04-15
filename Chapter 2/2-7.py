#!/usr/bin/env python

# Get input from user
input = raw_input('Enter some input: ')

# Print out each character from the input using a WHILE loop
ch = 0
while ch < len(input):
    print input[ch],
    ch += 1
print '\n'

#Print out each character from the input using a FOR loop
for c in input:
    print c,
print '\n'

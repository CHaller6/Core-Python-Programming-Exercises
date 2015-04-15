#!/usr/bin/env python
try:
    input = raw_input('Please input any positive or negative integer: ')
    num = int(input)
except ValueError, e:
    print 'The input was of the wrong format. Please input an integer less than, greater than, or equal to 0.'

output = ''
if num < 0:
    output = 'The number is less than 0'
elif num == 0:
    output = 'The number is exactly 0'
else:
    output = 'The number is greater than 0'

print output

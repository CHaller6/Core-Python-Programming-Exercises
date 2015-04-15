#!/usr/bin/env python

####
# Use raw_input() to prompt for a number between 1 and 100. If the input
# matches criteria, indicate so on the screen and exit. Otherwise,
# display an error and reprompt the user until the correct input is received.
####

success = False

while success == False:
    try:
        input = raw_input("Please enter a number between 1 and 100:")
        user_num = int(input)
        if user_num < 1 or user_num > 100:
            success = False
        else:
            print "Thank you for entering a proper number between 1 and 100"
            success = True
    except ValueError, e:
        success = False

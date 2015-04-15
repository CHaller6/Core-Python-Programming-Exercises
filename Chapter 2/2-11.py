#!/usr/bin/env python

#============================================================================
#============================================================================
# Author: Chris Haller
# Date: 9-13-14
# Exercise 2-11 from Chapter 2 of Core Python Programming, by Wesley J. Chun
#
#
# Exercise Description:
#
# "Take your solutions to any number of the previous five problems and upgrade
# your program to present a menu-driven text-based application that presents
# the user with a set of choices, e.g., (1) sum of five numbers, (2) average
# of five numbers, ... (X) Quit. The user makes a selection, which is then
# executed. The program exits when the user chooses the "quit" option. The
# great advantage of a program like this is that it allows the user to run as
# many iterations of your solutions without necessarily having to restart the
# same program over and over again. (It is also good for the developer who is
# usually the first user and tester of their applications!)"
#============================================================================
#============================================================================



##############################################################
# This determines whether an input number is between 1 and 100
##############################################################
def isInRange():
    "This function takes an input number from the user, and indicates success if the number is in the proper range, and failure if not."

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
            return




##########################
# This counts from 0 to 10
##########################
def countZeroToTen():
    "This function counts from 0 to 10 and prints the output."
    MAX = 11

    for c in range(11):
        print c,
    print

    return




###################################################################
# Determines whether an input number is positive, negative, or zero
###################################################################
def determineBoolean():
    "This function determines whether an input number is positive, negative, or zero"

    try:
        input = raw_input('Please input any positive or negative integer: ')
        num = int(input)
    except ValueError, e:
        print 'The input was of the wrong format. Please input an integer less than, greater than, or equal to 0.'
        return

    output = ''
    if num < 0:
        output = 'The number is less than 0'
    elif num == 0:
        output = 'The number is exactly 0'
    else:
        output = 'The number is greater than 0'
    print output




#################################################
# Display an input string one character at a time
#################################################
def displayChars():
    "This function displays the characters of a string input by a user one at a time."
    # Get input from user
    input = raw_input('Enter some input: ')

    #Print out each character from the input using a FOR loop
    for c in input:
        print c,
    print '\n'




##############################
# Print out five input numbers
##############################
def printFiveNum():
    "Prints out five integers input by the user."
    
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
        return
    ourTuple = (num1, num2, num3, num4, num5)
    
    #Print out the ruple using a WHILE loop
    print '\nTuple output: '
    cur = 0
    while cur < len(ourTuple):
        print ourTuple[cur],
        cur += 1
    print '\n'




#############################################
# Determine the average of five input numbers
#############################################
def determineAvg():
    "Determines and prints the average of five numbers input by the user."

    # Acquire the five integers from the user
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
        return
    ourList = [num1, num2, num3, num4, num5]

    # Determine the average of the five numbers.
    sum = 0
    for num in ourList:
        sum += num
    average = float(sum) / len(ourList)

    #Print out the list using a WHLIE loop
    print '\nList output: '
    cur = 0
    while cur < len(ourList):
        print ourList[cur],
        print ", "
        cur += 1
    print " is ", average
    print '\n'




########
# Main #
########
print "Welcome!\n\n"

exit = False
while exit == False:
    print "\n\nPlease choose from one of the options below:\n"
    # Option 1:
    print "     (1) Determine whether an input number is between 1 and 100"
    # Option 2:
    print "     (2) Count from 0 to 10"
    # Option 3:
    print "     (3) Determine if an input number is positive, negative, or zero"
    # Option 4:
    print "     (4) Display the characters of an input string"
    # Option 5:
    print "     (5) Display five input numbers"
    # Option 6:
    print "     (6) Determine the average of five input numbers"
    # Option 7:
    print "     (X) Exit the program\n"

    menu_input = raw_input("Please select a number to choose an option: ")
    if menu_input == 'X' or menu_input == 'x':
        print "\nThank you for using this program!\n\n\n"
        exit = True
    elif menu_input == '1':
        print "\n\n"
        isInRange()
    elif menu_input == '2':
        print "\n\n"
        countZeroToTen()
    elif menu_input == '3':
        print "\n\n"
        determineBoolean()
    elif menu_input == '4':
        print "\n\n"
        displayChars()
    elif menu_input == '5':
        print "\n\n"
        printFiveNum()
    elif menu_input == '6':
        print "\n\n"
        determineAvg()
    else:
        continue

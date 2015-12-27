## Program name: bool.py
## By Roger Stillick
## UoPeople CS-1101 Programming Fundamentals Unit 6 Programming Assignment
## December 2015
##
## The purpose of this program is to demonstrate, using comparison
## operators and if statments to compare two numbers that were inputed
## by the user.

## Compare function, compares two numbers and returns 1, 0, or -1,
## depending on the condition.
def compare(a, b):

    if a > b:
        return 1

    elif a == b:
        return 0

    elif a < b:
        return -1

## This function gets the input for the two numbers, and takes them in
## as a float.  The try/except statements ensures that only valid
## numbers are accepted.
def get_number(value):

        
    while True:
        try:
            print('Please enter the', value, 'number: ')
            number = float(input())
            return number
            break
            
        except ValueError:
            print('Not a valid number! Please try again ...')
            

## This is the main part of the program.  

a = get_number('first')
b = get_number('second')
result = compare(a, b)

print(result)


    

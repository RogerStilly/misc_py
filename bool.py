## Program name: bool.py
## Programming Fundamentals CS-1101
## University of the People (UoPeople)
## Dec 2015
##
## Purpose: demonstrate, using comparison operators and if statments to 
## compare two numbers that were inputed by the user.
##
##
def compare(a, b):

    if a > b:
        return 1

    elif a == b:
        return 0

    elif a < b:
        return -1

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


    

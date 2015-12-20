## Program name: mycalc.py
## Programming Fundamentals CS-1101
## University of the People (UoPeople)
## Dec 2015
##
## Purpose: create a calculator. This was challenging, because many
## bugs presented themselves, such as dividing by zero, or when using
## big numbers or numbers with decimal points. The most dificult problem
## was how to format the output of the numbers.
##
## 
def times(number1, number2):
    out = number1 * number2
    op = '*'
    output(number1, number2, op, out)

def div(number1, number2):
    out = number1 / number2
    op = '/' 
    output(number1, number2, op , out)

def add(number1, number2):
    out = number1 + number2
    op = '+'
    output(number1, number2, op, out)

def sub(number1, number2):
    out = number1 - number2
    op = '-'
    output(number1, number2, op, out)

def menu():

    operation = 0
    while operation == 0:
        print()
        print('''Select an operation:

        1)  addition
        2)  subtraction
        3)  multiplication
        4)  division
        5)  quit and exit the program

            ''')
                  
        operation = input('Enter your choice 1-5: \n')
        
        if operation in ('1', '2', '3', '4', '5'):
                return operation

        else:
            operation = 0
            print("Only 1-5, try again... \n\n")

def get_number(operand):
# try/except statement, first checks if number is a float, then an int,
# if that doesn't work, it throughs the exception, and loops back
# to the while statement to ask for the input again.
# I was able to use the parameter to pass a string I called 'operand'
# to the function, and used that in the print statement to customize
# which number to ask for, either the first or second.
    while True:
        try:
            print('Please enter the', operand, 'number: ')
            number = input()
            number = float(number)
            if number == int(number):
                return int(number)
            break
            
        except ValueError:
            print("Not a valid number! Please try again ...")
            
    return number

def selection(number1, number2, operation):
# This function takes the selected operation from the selection()
# function and calls the corresponding function for the math operation.
# If operation 5 is selection, which is the option to quit, then the
# function returns a 'q', which will cause the while loop in the main
# body of the program to be bypassed, and effectively end the program.
    while True:
        if operation == '1':
            add(number1, number2)
            break
            
        elif operation == '2':
            sub(number1, number2)
            break

        elif operation == '3':
            times(number1, number2)
            break

        elif operation == '4':
            try:
                div(number1, number2)
                break
            
            except ZeroDivisionError:
                print()
                print(number1, "/ 0 = Undefined")
                break        

        elif operation == '5':
            cont = 'q'
            return cont
            break
        
def output(number1, number2, op, out):

    n1 = (number1)
    n2 = (number2)

#    print()    
#    print(n1, op, n2, '= ', out)
# I took the opportunity to mess around with formatting
# I chose to use the :1.12G format because I liked the E notation for very
# small numbers, rather than the e notation.
    print()
    print('{:1.12G}'.format(n1), op, '{:1.12G} = {:1.12G}'.format(n2, out))
    
def control():
# This function controls everything. I decided to make this a funtion,
# because I feel like I can reuse this control function for later in
# the course. Before, it was just the main body of the program...
    cont = ''

    while cont != 'q':

        number1 = get_number('first')
        operation = menu()
        if operation == '5':
            cont = 'q'
            
        else:   
            number2 = get_number('second')
            cont = selection(number1, number2, operation)
            
            if cont != 'q':        
                cont = input("\nAny key to continue using, 'q' to quit: \n" )

                if cont == 'q' or cont == 'Q':
                    cont = 'q'

#This is the main body of the program.  Only one function call.
control()

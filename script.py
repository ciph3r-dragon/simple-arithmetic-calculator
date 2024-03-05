#Algorithm for the Arithmetic Calculator 

#1-Start the program
#2-Take two numbers as input using input() function
#3-Take operation to be performed using input() function
#4-Use conditional logic, if-else to select the operation to perform on the two operands
#5-Store the computed value in an object named result
#6-Print result
#7-Loop the program to restart after every successful run
#8-End program

while True:

    x = float(input('Enter first number: '))
    y = float(input('Enter second number: '))

    operation = input("Enter the operation you want to perfrom ('+', '-', '*', '/', '%', '**'):")

    result = 0

    if operation == '+':
        result = x + y

    elif operation == '-':
        result = x - y

    elif operation == '*':
        result = x * y

    elif operation == '/':
        result = x / y

    elif operation == '%':
        result = x % y

    elif operation == '**':
        result = x ** y

    else: 
        print('Invalid Input')

    print('Your answer is: ', result)
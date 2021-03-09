'''
Write a program that serves as a basic calculator. It asks for two
numbers, then it asks for an operator. Gracefully deal with input that
doesn't cleanly convert to numbers. Deal with division by zero errors.
'''


def calculator(number1,number2,operation):
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '*':
        return number1 * number2
    else:
        try:
            return number1 / number2
        except ZeroDivisionError:
            return "Cannot divide by zero"


number1 = int(input("Enter first number : "))
number2 = int(input("Enter second number : "))
operation = input("Enter + or - or * or / : ")
print(calculator(number1,number2,operation))
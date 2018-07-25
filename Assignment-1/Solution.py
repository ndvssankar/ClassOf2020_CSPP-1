''' Exercise: Assignment-1.'''
# Write a Python function, factorial(n), that takes in one number and returns
# the factorial of given number.

# This function takes in one number and returns one number.

import math

def factorial(value):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    return math.factorial(value)


def main():
    ''' Reading the data from the input and passing to the function factorial.'''
    data = input()
    for i in range(int(data)):
        value = input()
        print(factorial(int(value)))

if __name__ == "__main__":
    main()

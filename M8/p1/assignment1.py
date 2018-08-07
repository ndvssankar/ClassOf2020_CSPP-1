'''Exercise: Assignment-1'''
# Write a Python function, factorial(n),
# that takes in one number and returns the factorial of given number.

# This function takes in one number and returns one number.


def factorial(number):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    if number == 1 or number == 0:
        return 1
    else:
        return number * factorial(number-1)



def main():
    '''This is a main function'''
    number = input()

    print(factorial(int(number)))

if __name__ == "__main__":
    main()

# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number and returns the sum of digits of given number.

# This function takes in one number and returns one number.

s = 0
def sumofdigits(n):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if n != 0:
        return s
    else:
        r = n%10
        s += r
        return sumofdigits(n/10)

def main():
    number = input()
    print(sumofdigits(int(number)))

if __name__== "__main__":
    main()


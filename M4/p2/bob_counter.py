'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    ''' Finds the number of occurances of the bob.'''
    string = input()
    # the input string is in s
    # remove pass and start your code here
    count = 0
    index = string.find("bob")
    while index >= 0:
        count = count + 1
        index = string.find("bob", index+1)
    print(count)

if __name__ == "__main__":
    main()

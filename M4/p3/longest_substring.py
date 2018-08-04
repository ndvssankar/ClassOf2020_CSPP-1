'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.'''

def get_longest_string(string, index):
    count = 0
    for i in range(index, len(string)-1):
        if string[i] <= string[i+1]:
            count = count + 1
        else:
            break
    return count+1


def main():
    ''' This method finds the longest substring.'''
    string = input()
    # the input string is in s
    # remove pass and start your code here
    len1 = get_longest_string(string, 0)
    longest_alphabet_string = string[0:len1]
    print(longest_alphabet_string)
    index = 0
    print(len1)
    for i in range(len(string)):
        len2 = get_longest_string(string, len1 + i)
        longest_alphabet_string = string[len1 : len1+len2]
        print(longest_alphabet_string)
        print(len2)
        len1 = len2
        # if len1 < len2:
        #     longest_alphabet_string = string[len1+1 : len2]
        #     len1 = len2
        # else:
        #     longest_alphabet_string = string[]
        #     len1 = 
        # print(longest_alphabet_string)
if __name__ == "__main__":
    main()

'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def tokenize(string):
    # print(string)
    regex = re.compile('[^a-zA-Z0-9]')
    string = regex.sub(' ', string.strip())
    # print(string)
    return string.split()

def main():
    number_of_lines = int(input())
    d = {}
    for i in range(number_of_lines):
        strings = tokenize(input())
        for string in strings:
            if string in d:
                d[string] += 1
            else:
                d[string] = 1
    print(d)

if __name__ == '__main__':
    main()

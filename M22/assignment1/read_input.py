'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    number_of_lines = int(input())
    string = ""
    for i in range(number_of_lines):
	    string += input()
	    string += "\n"
    print(string)
if __name__ == '__main__':
    main()

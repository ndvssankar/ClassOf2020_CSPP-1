'''
Given a  number int_input, find the product of all the digits
example: 
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    product = 1
    flag = False
    if int_input < 0:
        flag = True
        int_input = -int_input
    if int_input == 0:
        print(0)
    else:
        while int_input != 0:
            rem = int_input % 10
            product = product * rem
            int_input = int_input // 10
        if flag:
            print(-product)
        else:
            print(product)

if __name__ == "__main__":
    main()

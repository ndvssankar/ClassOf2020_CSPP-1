'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_line(line):
    '''
        Checks the line of the sudoku is valid or not.
    '''
    for _, value in enumerate(line):
        # print(line.count(line[i]), end=" ")
        if line.count(value) != 1:
            return False
        if int(value) <= 0 or int(value) >= 10:
            return False
    return True

# def check_grid(sudoku):
#     '''
#         Check the grid is valid or not.
#     '''
#     for i in range(3):
#         line = ""
#         for j in range(3):
#             line += sudoku[i][j]
#             if check_line(line) == False:
#                 return False
#     return True

def check_horizontal(sudoku):
    '''
        Check the horizontal line of sudoku is valid or not.
    '''
    for line in sudoku:
        if not check_line(line):
            return False
    return True

def check_vertical(sudoku):
    '''
        Checks whether the vertical line of sudoku is valid or not.
    '''
    for i in range(len(sudoku)):
        string = ""
        for line in sudoku:
            string += line[i]
        if not check_line(string):
            return False
    return True

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    if not check_horizontal(sudoku):
        return False
    elif not check_vertical(sudoku):
        return False
    return True

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''

    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for _ in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()

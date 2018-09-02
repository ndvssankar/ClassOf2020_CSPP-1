def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(m1[0]) == len(m2):
        result = []
        for i in range(len(m1)):
            lst = []
            for j in range(len(m2[0])):
                s = 0
                for k in range(len(m2)):
                    s += m1[i][k] * m2[k][j]
                lst.append(s)
            result.append(lst)
        return result
    else:
        print("Error: Matrix shapes invalid for mult")
        return None

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        result = []
        for i in range(len(m1)):
            lst = []
            for j in range(len(m2[0])):
                lst.append(m1[i][j] + m2[i][j])
            result.append(lst)
        return result
    else:
        print("Error: Matrix shapes invalid for addition")
        return None

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    line = input().split(",")
    rows = int(line[0])
    cols = int(line[1])
    matrix = []
    for i in range(rows):
        line = input().split(" ")
        if len(line) != cols:
            print("Error: Invalid input for the matrix")
            return None
        else:
            matrix.append([int(j) for j in line])
    return matrix



def main():
    # read matrix 1
    m1 = read_matrix()

    # read matrix 2
    m2 = read_matrix()

    
    if m1 != None and m2 != None:
        # add matrix 1 and matrix 2
        print(add_matrix(m1, m2))

        # multiply matrix 1 and matrix 2
        print(mult_matrix(m1, m2))
    

if __name__ == '__main__':
    main()

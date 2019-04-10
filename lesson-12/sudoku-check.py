# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

def sudoku_transform(sudoku):
    #this function transposes the original sudoku square, backwards, to allow
    #for checking the columns separately from the rows, but using row logic for both

    #Establish the size of the sudoku square, which will initiliaze all counts
    size = len(sudoku)

    #initialize the "new" sudoku square, which will hold the new rows to check
    new_sudoku = [[] for i in range(size)]
    new_row = 0
    mutable_sudoku = list(sudoku)

    print 'sudoku location is ', hex(id(sudoku))
    print 'mutable_sudoku location is ', hex(id(mutable_sudoku))

    print 'mutable_sudoku is ', mutable_sudoku

    for row in mutable_sudoku:
        while row:
            new_sudoku[new_row].append(row.pop())
            new_row += 1
        new_row = 0

    print 'now mutable_sudoku is ', mutable_sudoku
    print 'also, sudoku is ', sudoku
    return new_sudoku

def check_sudoku(sudoku):
    #Establish the size of the sudoku square, which will initiliaze all counts
    size = len(sudoku)

    #get the transformed sudoku to check columns later
    column_check = sudoku_transform(sudoku)

    #now we check the original Sudoku's rows
    count = 1

    for row in sudoku:
        print row
        for num in row:
            while count < len(row):
                if row[0] == row[count]:
                    return False
                else:
                    count +=1
            row.pop(0)
            print row


    # i = 0 #row count
    # j = 0 #column count
    #
    # while i < len(sudoku):
    #     while j < len(sudoku):
    #         if sudoku[i, j] = sudoku[i, j + 1]:
    #             return False
    #         j = j + 1

    # for row in sudoku:
    #     #take each item in row and check for equality against other items in row
    #     for num in row:









print check_sudoku(incorrect)
#>>> False

#print check_sudoku(correct)
#>>> True

#print check_sudoku(incorrect2)
#>>> False

#print check_sudoku(incorrect3)
#>>> False

#print check_sudoku(incorrect4)
#>>> False

#print check_sudoku(incorrect5)
#>>> False

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

incorrect6 = [[ 2, 1, 3 ],
            [ 3, 1, 2 ],
            [ 2, 3, 1 ]]

def check_sudoku(sudoku):
    #Establish the size of the sudoku square, which will initiliaze all counts
    size = len(sudoku)

    #now we check the Sudoku's rows

    for row in range(size):
        for col in range(size-1):

            #first, check for quality of data
            if sudoku[row][col] > size or sudoku[row][col+1] > size:
                return False
            if type(sudoku[row][col]) != int or type(sudoku[row][col+1]) != int:
                return False
            if sudoku[row][col] < 1 or sudoku[row][col+1] < 1:
                return False

            #then, check for equality
            for i in range(1,size - col):
                if sudoku[row][col] == sudoku[row][col+i]:
                    return False


    #now we check the columns - same as above, but with row and col reversed.
    #don't need to check for data quality; if we've made it here, we're good!

    for col in range(size):
        for row in range(size-1):
            # if sudoku[row][col] == sudoku[row+1][col]:
            #     return False
            for i in range(1,size - row):
                # print 'i is ', i
                if sudoku[row][col] == sudoku[row+i][col]:
                    return False

    return True

print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

#print check_sudoku(incorrect2)
#>>> False

#print check_sudoku(incorrect3)
#>>> False

#print check_sudoku(incorrect4)
#>>> False

#print check_sudoku(incorrect5)
#>>> False

print check_sudoku(incorrect6)
#>>> False

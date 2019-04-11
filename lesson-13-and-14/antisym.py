# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True
# if the given square is antisymmetric and False otherwise.
# An nxn square is called antisymmetric if A[i][j]=-A[j][i]
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(list):
    #Write your code here
    # First, we will check to make sure that the array is not empty and is square.
    if len(list) == 0:
        return True

    if len(list) != len(list[0]):
        return False

    #In an antisymmetric array (yeah okay not a python array, but like a math array),
    #each digit is identical to the digit in the "opposite" location.  For example,
    #the digit in row 2, column 3 must be equal to the digit in row 3, column 2.

    #So, check that we have that!

    for i in range(len(list)):
        for j in range(len(list)):
            if list[i][j] != -list[j][i]:
                return False

    return True

# Test Cases:

print antisymmetric([[0, 1, 2],
                     [-1, 0, 3],
                     [-2, -3, 0]])
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, 2],
                     [-1, 0, -2],
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False

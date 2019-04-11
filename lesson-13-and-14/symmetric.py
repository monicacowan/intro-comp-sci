# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(list):
    # First, we will check to make sure that the array is not empty and is square.
    if len(list) == 0:
        return True

    if len(list) != len(list[0]):
        return False

    #In a symmetric array (yeah okay not a python array, but like a math array),
    #each digit is identical to the digit in the "opposite" location.  For example,
    #the digit in row 2, column 3 must be equal to the digit in row 3, column 2.

    #So, check that we have that!

    for i in range(len(list)):
        for j in range(len(list)):
            if list[i][j] != list[j][i]:
                return False

    return True

print symmetric([[1, 2, 3],
               [2, 3, 4],
               [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
               ["dog", "dog", "fish"],
               ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
               ["dog", "dog", "dog"],
               ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
               [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
               [2, 3, 4, 5],
               [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False

print symmetric([])
#>>> False

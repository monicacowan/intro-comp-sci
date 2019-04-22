# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def shift_n_letters(letter, n):

    newOrd = ord(letter) + n

    if newOrd > 122:
        diff = newOrd - 122
        newOrd = 96 + diff % 26 # <-- cycles through the alphabet starting at a
    if newOrd < 97:
        diff = 97 - newOrd
        newOrd = 123 - diff % 26 # <-- cycles through alphabet backwards from z
    return chr(newOrd)

def rotate(name, num):
    rotatedName = ""
    # Cycle through each character in the name
    for letter in name:
        if letter != " ":
            rotatedName += shift_n_letters(letter, num)
        else:
            rotatedName += letter
    return rotatedName

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
print rotate ('this course teaches you to code', 7)
#>>> 'aopz jvbyzl alhjolz fvb av jvkl'

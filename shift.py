# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):

    newOrd = ord(letter) + n

    if newOrd > 122:
        diff = newOrd - 122
        newOrd = 96 + diff % 26 # <-- cycles through the alphabet starting at a
    if newOrd < 97:
        diff = 97 - newOrd
        newOrd = 123 - diff % 26 # <-- cycles through alphabet backwards from z
    return chr(newOrd)

print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i
print shift_n_letters('a', -1)
#>>> z
print shift_n_letters('z', 26)
#>>> z

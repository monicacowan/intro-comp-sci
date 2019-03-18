#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------
#                             Sum                123
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a
# given positive integer value.
#
# Ranking
# 1 STAR: solved the problem!
# 2 STARS: 6 < lines <= 9
# 3 STARS: 3 < lines <= 6
# 4 STARS: 0 < lines <= 3

def print_abacus(value):
       #
       #the key here will be determining how big the number is, in terms of 10's
       # and then determining how to get the print pattern right.

       #First step: print the unchanged lines.  Find the length of value, and
       #print any rows above the length of the value
       lengthValue = len(str(value))

      #print all of the unchanged rows
       while lengthValue < 10:
           print '|00000*****   |'
           lengthValue += 1

       #Now for the harder part: how to make the abacus lines.  Get a multiplier
       #based on the digit.  If it's under or = 5, only stars; if it's over 5,
       #then it will be a combo of stars and zeroes.

       lengthValue = len(str(value)) #reinitialize
       multipler = 0

       while lengthValue > 0:    #starts with the highest digit

           exponent = lengthValue - 1
           valueModLength = value % (10**exponent)

           abacusDigit = (value - valueModLength)/(10**exponent)

           #now that we have the digit we need to represent, get combo of * and 0:

           if abacusDigit <= 5:
               print '|00000' + '*'*(5 - abacusDigit) + " "*3 + '*'*abacusDigit + '|'
           else:
               print '|' + '0'*(10 - abacusDigit) + " "*3 + '0'*(abacusDigit-5) + '*****|'

           lengthValue -= 1 #move on to the next 10's place down
           value = value - abacusDigit * (10**exponent) #get rid of the value we just represented


       #

###  TEST CASES
print "Abacus showing 0:"
print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
print "Abacus showing 12345678:"
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
print "Abacus showing 1337:"
print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|

# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.

# If a number x in the string is less than or equal
# to the preceding number y, the number x should be inserted
# into a sublist.

#Continue adding the following numbers to the
# sublist until reaching a number z that
# is greater than the number y.
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number

def numbers_in_lists(string):

    #initialize the string!
    numString = []

    #We'll want to initialize a count, to keep track of where we are
    #if we are in an inner string.
    count = 0

    for i in range(len(string)):

        #put the first number in the numString
        if i == 0:
            numString.append(int(string[i]))

        if i > 0:  #all other numbers...

            #simple case: if the next number is bigger that the previous, just append it
            #if int(string[i]) > int(string[i-1]):

            if int(string[i]) > numString[len(numString)-1]:
                numString.append(int(string[i]))
                #re=initialize count to zero; we're out of the inner list!
                count = 0

            else:
                #3 situations:
                #First: we start a new list (count is zero)
                #Second: we escape the inner list b/c the number is big enough
                #Third: or we append to the current inner list (count greater than zero)

                if count == 0:
                    numString.append([int(string[i])])
                    count += 1

                elif int(string[i]) > numString[len(numString)-2]:
                    numString.append(int(string[i]))

                    #re=initialize count to zero; we're out of the inner list!
                    count = 0

                else:  #we only hit this if we've already started a new inner list.
                    #print type(numString[len(numString)-1]), numString[len(numString)-1], 'count is ', count
                    numString[len(numString)-1].append(int(string[i]))
                    count += 1


    return numString
    #print "length is ", len(numString)
    #print "the value at the length minus one is ", numString[len(numString)-1]

#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print repr(string), numbers_in_lists(string) == result
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result

# string = '4555123266'
# result = [4, 5, [5, 5, 1, 2, 3, 2], 6, [6]]
# numbers_in_lists(string)

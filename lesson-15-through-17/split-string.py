# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.


def split_string(source,splitlist):

    #first, let's make a list of the characters in split list.
    splitChar = []
    for i in range(len(splitlist)):
        splitChar.append(splitlist[i])


    #next, we'll cycle through the source string and check each character
    #against the split list.

    prev_end = 0 # <--- will keep track of where the last string ended
    str_length = 0 # <--- keeps track of the length of the current string
    splitString = [] # <--- initializes the answer list

    for i in range(len(source)):
        if source[i] not in splitChar:
            str_length += 1

            #Need to catch the cases which don't end with a split char.  Since
            #we only get here if the last character isn't a split, append the
            #last string:

            if i == len(source) - 1:
                splitString.append(source[prev_end:(prev_end + str_length)])

        else: # <--- only get here if the char is in splitChar

            #Only append if the string length is greater than 0.  Otherwise,
            #the previous character was also a split char!
            if str_length > 0:
                splitString.append(source[prev_end:(prev_end + str_length)])

            prev_end = i + 1 # <--- this marks the last point a split char was seen
            str_length = 0

    return splitString

out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']

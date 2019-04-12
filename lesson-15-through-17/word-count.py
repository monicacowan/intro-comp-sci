# Write a procedure, count_words, which takes as input a string
# and returns the number of words in the string. You may consider words
# as strings of characters separated by spaces.

def count_words(source):
    #This is based off of the split-string.py code.  Just get the length!

    splitChar = [' ']


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

    return len(splitString)


passage =("The number of orderings of the 52 cards in a deck of cards "
"is so great that if every one of the almost 7 billion people alive "
"today dealt one ordering of the cards per second, it would take "
"2.5 * 10**40 times the age of the universe to order the cards in every "
"possible way.")
print count_words(passage)
#>>>56

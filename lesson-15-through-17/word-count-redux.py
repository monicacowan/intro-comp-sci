# Write a procedure, count_words, which takes as input a string
# and returns the number of words in the string. You may consider words
# as strings of characters separated by spaces.

def count_words(source):
    # An attempt to simplify... if a character is a space, it means a word has
    # ended.  For each space, increase the word count.

    count = 0

    for i in range(len(source)):
        if source[i] == ' ':
            count += 1

    # This handles the empty string case.
    if len(source) == 0:
        return 0

    else:
        return count + 1 # <-- adding 1 to account for last word in string.


passage =("The number of orderings of the 52 cards in a deck of cards "
"is so great that if every one of the almost 7 billion people alive "
"today dealt one ordering of the cards per second, it would take "
"2.5 * 10**40 times the age of the universe to order the cards in every "
"possible way.")
print count_words(passage)
#>>>56

passage2 = ''
print count_words(passage2)

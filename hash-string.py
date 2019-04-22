# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.

def hash_string(keyword,buckets):
    #first, convert the keyword into a number based on the sum of the characters
    sum = 0

    for letter in keyword:
        sum += ord(letter)

    #the bucket is defined as the modulo of sum and buckets
    return sum % buckets



print hash_string('a',12)
#>>> 1

print hash_string('b',12)
#>>> 2

print hash_string('a',13)
#>>> 6

print hash_string('au',12)
#>>> 10

print hash_string('udacity',12)
#>>> 11

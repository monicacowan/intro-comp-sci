# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(p, value):
    ##using index:

    if value in p:
        return p.index(value)

    return -1

    ##not using index:
    # count = 0
    # present = False
    #
    # for i in p:
    #     if i == value:
    #         return count
    #         present = True
    #     count += 1
    #
    # if present == False:
    #     return -1

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1

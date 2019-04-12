# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []

def add_to_index(index,keyword,url):
    #we know the first entry just needs to be added.
    if len(index) == 0:
        index.append([keyword,[url]])

    #first, check to see if that keyword is already in the index.  If yes,
    #add to the existing list of urls.

    else:
        #initialize count, which if nonzero, means that we've checked a certain
        #number of entries.
        count = 0

        for entry in index:
            if keyword in entry:
                entry[1].append(url)

            else:
                count += 1  #so we can keep track of how many entries we've looked at

        #this checks to see if we've cycled through all of the entries.  If we have,
        #that means that the keyword doesn't exist yet, so let's append!

        if count == len(index):
            index.append([keyword,[url]])


add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']],
#>>> ['computing', ['http://acm.org']]]

# Define a procedure,

# hashtable_lookup(htable,key)

# that takes two inputs, a hashtable
# and a key (string),
# and returns the value associated
# with that key.

def hashtable_lookup(htable,key):
    #First, find the location of the bucket if the key were to be in the Table
    location = hash_string(key, len(htable))

    #if the key is in the table, we want to return whatever it's associated with
    for item in htable[location]: # <-- cycle through the paired lists...
        if item[0] == key:
            return item[1]

    #We only get here if the key is never matched, ie, key isn't in the table
    return None

def hashtable_add(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    bucket.append([key,value])


def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table


table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

print hashtable_lookup(table, 'Monica')
#>>> 13

print hashtable_lookup(table, 'Louis')
#>>> 29

print hashtable_lookup(table, 'Zoe')
#>>> 14

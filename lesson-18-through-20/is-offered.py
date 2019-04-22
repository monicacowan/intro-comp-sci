# Dictionaries of Dictionaries (of Dictionaries)

# The next several questions concern the data structure below for keeping
# track of Udacity's courses (where all of the values are strings):

#    { <hexamester>, { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }

#For example,

courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253':
                {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262':
                {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                 'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }

# If you want to loop through the keys in the dictionary,
# you can use the construct below.
#         for <key> in <dictionary>:
#                    <block>
# For example, this procedure returns a list of all the courses offered
# in the given hexamester:

def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res

# You do not need to use this code if you do not want to and may find another,
# simpler method to answer this question, although later ones may require this.

# Define a procedure, is_offered(courses, course, hexamester), that returns
# True if the input course is offered in the input hexamester, and returns
# False otherwise.  For example,

#print is_offered(courses, 'cs101', 'apr2012')
#>>> True

#print is_offered(courses, 'cs003', 'apr2012')
#>>> False

# (Note: it is okay if your procedure produces an error if the input
# hexamester is not included in courses.
# For example, is_offered(courses, 'cs101', 'dec2011') can produce an error.)
# However, do not leave any uncommented statements in your code which lead
# to an error as your code will be graded as incorrect.

def is_offered(courses, course, hexamester):
    if hexamester in courses:
        if course in courses[hexamester]:
            return True
    return False

# Define a procedure, when_offered(courses, course), that takes a courses data
# structure and a string representing a class, and returns a list of strings
# representing the hexamesters when the input course is offered.

def when_offered(courses,course):
    offered = [] # <-- initialize the list of strings of hexamesters
    for hexamester in courses:
        if course in courses[hexamester]:
            offered.append(hexamester)
    return offered

# [Double Gold Star] Define a procedure, involved(courses, person), that takes
# as input a courses structure and a person and returns a Dictionary that
# describes all the courses the person is involved in.  A person is involved
# in a course if they are a value for any property for the course.  The output
# Dictionary should have hexamesters as its keys, and each value should be a
# list of courses that are offered that hexamester (the courses in the list
# can be in any order).

def involved(courses, person):
    involvement = {}

    # Cycle through the hexamesters, first
    for hexamester in courses:
        # Now, cycle through each course.
        for course in courses[hexamester]:
            # lastly, look for the person in each key.
            for value in courses[hexamester][course]:
                if courses[hexamester][course][value] == person:
                    # We get to this step if the person is involved.  But, first
                    # need to check to see if the person was already involved, which
                    # would mean that there is a value in involvement for this
                    # hexamester already.
                    # involvement[hexamester] = [course]

                    if hexamester in involvement:
                        involvement[hexamester].append(course)

                    else:
                        involvement[hexamester] = [course]

    return involvement


# For example:

# print involved(courses, 'Dave')
#>>> {'apr2012': ['cs101', 'cs387'], 'feb2012': ['cs101']}

# print involved(courses, 'Peter C.')
#>>> {'apr2012': ['cs262'], 'feb2012': ['cs101']}

# print involved(courses, 'Dorina')
#>>> {'jan2044': ['cs001']}

# print involved(courses,'Peter')
#>>> {}

#print involved(courses,'Robotic')
#>>> {}

#print involved(courses, '')
#>>> {}




# print when_offered (courses, 'cs101')
# #>>> ['apr2012', 'feb2012']
#
# print when_offered(courses, 'bio893')
# #>>> []


# print is_offered(courses, 'cs101', 'apr2012')
# #>>> True
#
# print is_offered(courses, 'cs003', 'apr2012')
# #>>> False
#
# print is_offered(courses, 'cs001', 'jan2044')
# #>>> True
#
# print is_offered(courses, 'cs253', 'feb2012')
# #>>> False

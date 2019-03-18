# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#

def leapYear(year):
    #This procedure determines whether or not a year is a leap year.
    #Returning True means the year is a leap year; False means it is not.
    #First, a leap year must be divisible by 4
    if year%4 > 0:
        return False
        #if the year is divisible by 4 and also 100, it's a leap year
    elif year%100 > 0:
        return True
        #if the year is divisible by 4 and NOT by 400, then it isn't a leap year
    elif year%400 > 0:
        return False
        #and if it's divisible by 4, but not by 100 or 400, then leap year!
    else:
        return True

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    print "tbd!"
    ##

#print leapYear(2000)


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

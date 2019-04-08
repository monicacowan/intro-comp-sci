###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###
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

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    #this returns true if the first date is before the second
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysInMonth(year, month):
    #return 30
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    if month == 2 and leapYear(year):
        return 29
    if month == 2:
        return 28
    else:
        return 31

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE

    if day < daysInMonth(year, month):
        return year, month, day + 1
    elif month == 12:
        return year + 1, 1, 1
    else:
        return year, month + 1, 1

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    assert year1 <= year2

    if year1 == year2:
        assert month1 <= month2
        if month1 == month2:
            assert day1 <= day2

    year, month, day = year1, month1, day1
    days = 0

    while (year, month, day) != (year2, month2, day2):
        days += 1
        year, month, day = nextDay(year, month, day)

    return days

def test():
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 1) == 0
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 2) == 1
    assert nextDay(2013, 1, 1) == (2013, 1, 2)
    assert nextDay(2013, 4, 30) == (2013, 5, 1)
    assert nextDay(2012, 12, 30) == (2012, 12, 31)
    print "u r done"

test()

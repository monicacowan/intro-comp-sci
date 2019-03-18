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

def numberOfDays(month, year):
    #this procedure returns the number of days in the month, including leaps

    if month == 1:
        return 31
    elif month == 2 and leapYear(year):
        return 29
    elif month == 2:
        return 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        return 31

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    #general strategy will be to compare year2 to year1 first
    #if year1 = year2, then we know that all we have to do is calc the
    #number of days between the dates:
    year_diff = year2 - year1

    if year_diff == 0:
        #add up the number of days since the 1st and subtract...
        month = month1 - 1  #this way we are only grabbing the total months
        days_total_1 = 0
        while month > 0:
            days_total_1 += numberOfDays(month, year1)
            month -= 1

        days_total_1 += day1

        month = month2 - 1  #this way we are only grabbing the total months
        days_total_2 = 0
        while month > 0:
            days_total_2 += numberOfDays(month, year2)
            month -= 1

        days_total_2 += day2

        return days_total_2 - days_total_1

    #okay, gets a bit more complicated when the years are different!  Could go
    #with: add up the total numbers of days left in the first year, get the
    #total number of days in between for the complete years, and then add the
    #number of days so far in the last year...

    else:
        days_total_1 = 0
        month = 12

        while month - month1 > 0: #if month1 is 12, will skip this loop
            days_total_1 += numberOfDays(month, year1)
            month -= 1

        #add on the remaining days in month1
        days_total_1 += numberOfDays(month1, year1) - day1
        #print "days left in the year: ", days_total_1

        #reset month counter, b/c we're looking at the 2nd year now!  Can use
        #the same calculation method as above to get the number of days since
        #the first...

        month = month2 - 1  #this way we are only grabbing the total months
        days_total_2 = 0

        while month > 0:
            days_total_2 += numberOfDays(month, year2)
            month -= 1

        days_total_2 += day2
        #print "days in the 2nd year so far: ", days_total_2

        #now, another if statement.  If we are only 1 year apart, just add the
        #values we just added.

        if year2 - year1 == 1:
            return days_total_2 + days_total_1

        else:

            #ok, now we have to figure out how many years are in between,
            #and for those years, add up the number of days total...
            currentYear = year2 -1
            days_total = 0

            while currentYear > year1:
                if leapYear(currentYear):
                    days_total += 366
                else:
                    days_total += 365

                currentYear -= 1

            return days_total + days_total_1 + days_total_2




    ##

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

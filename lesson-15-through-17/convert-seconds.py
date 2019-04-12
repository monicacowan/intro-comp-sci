# Write a procedure, convert_seconds, which takes as input a non-negative
# number of seconds and returns a string of the form
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes,
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(total_seconds):
    # Generally, the approach is to determine both the number and string associated
    # with each chunk of time measurement.

    # SECTION ONE: HOURS
    # If the total_seconds is less than 3600, no hours:

    if total_seconds < 3600:
        hr_num = 0
        hr_str = 'hours'

    else:
        hr_num = int(total_seconds / 3600)
        if hr_num == 1:
            hr_str = 'hour'
        else:
            hr_str = 'hours'

    total_seconds -= hr_num * 3600 # <-- reduce total seconds to the leftover

    hours = str(hr_num) + ' ' + hr_str

    # SECTION TWO: MINUTES
    # If the total_seconds is less than 60, no minutes:

    if total_seconds < 60:
        min_num = 0
        min_str = 'minutes'

    else:
        min_num = int(total_seconds / 60)
        if min_num == 1:
            min_str = 'minute'
        else:
            min_str = 'minutes'

    total_seconds -= min_num * 60

    minutes = str(min_num) + ' ' + min_str

    # SECTION THREE: MINUTES
    # If the total_seconds is 0, no seconds:

    if total_seconds == 0:
        sec_num = 0
        sec_str = 'seconds'

    else:
        sec_num = total_seconds
        if sec_num == 1:
            sec_str = 'second'
        else:
            sec_str = 'seconds'

    seconds = str(sec_num) + ' ' + sec_str

    return hours + ", " + minutes + ", " + seconds


print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds

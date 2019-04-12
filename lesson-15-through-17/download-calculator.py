# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).

unit_list = [ 'k', 'M', 'G', 'T']
mult_list = [10, 20, 30, 40]

def multiplier(size_tag):
    #returns the multiplier for bits as a function of the units.
    location = unit_list.index(size_tag[0])

    if size_tag[1] == 'b':
        return 2 ** mult_list[location]
    else:
        return 2 ** mult_list[location] * 8

def convert_seconds(total_seconds):
    # This procedure just formats a total number of seconds into hours, mins, secs
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
            sec_num = int(sec_num)
            sec_str = 'second'
        else:
            sec_str = 'seconds'

    seconds = str(sec_num) + ' ' + sec_str

    return hours + ", " + minutes + ", " + seconds

def download_time(file_size, file_size_units, bandwidth, bandwidth_units):
    # First, we'll calculate the total file size in bits.  Then, the total bandwidth
    # in bits/second.  The former divided by the latter gives us seconds, which
    # we will format using the convert_seconds function.

    # FILE SIZE CALCS
    file_bits = file_size * multiplier(file_size_units)

    # BANDWIDTH CALCS
    bandwidth_bits = bandwidth * multiplier(bandwidth_units)

    total_seconds = file_bits * 1.0 / bandwidth_bits #<-- we don't want integers.

    return convert_seconds(total_seconds)

print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

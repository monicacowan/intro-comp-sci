def stamps(n):
    five_pence = n / 5
    remainder = n % 5
    print "remainder is ", remainder

    two_pence = remainder / 2
    print "two pence is", two_pence

    if remainder % 2 == 1:
        one_pence = 1
    else:
        one_pence = 0

    return (five_pence, two_pence, one_pence)

print stamps(0)

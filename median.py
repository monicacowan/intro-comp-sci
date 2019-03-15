def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a, b, c):
    big_test1 = bigger(a, b)
    big_test2 = bigger(b, c)

    if big_test1 == big_test2:
        return bigger(a, c)
    else:
        return big_test1 + big_test2 - bigger(big_test1, big_test2)

print median(2, 12, 3)

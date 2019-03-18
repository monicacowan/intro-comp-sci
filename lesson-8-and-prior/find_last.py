def find_last(s, target):
    seed = s.find(target)

    if seed == -1:
        return seed
    else:
        while seed > -1:
            prev_loc = seed
            seed = s.find(target, seed+1)
        return prev_loc


print find_last("hello", "l")

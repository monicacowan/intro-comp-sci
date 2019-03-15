def set_range(a, b, c):
    biggest = max(a, b, c)
    smallest = min(a, b, c)

    return biggest - smallest

print set_range(1, 2, 3)

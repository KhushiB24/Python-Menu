def remainder(x, y):
    if x == 0:
        return x
    while y != 0:
        if y > x:
            x = x - y
        else:
            y = y - x
    return x
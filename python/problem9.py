def problem9():
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c for
    which a^2 + b^2 = c^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.

    Find the product a*b*c.
    """
    first_a = 0
    # the largest value of c that satisfies a < b < c is 999
    for c in xrange(2, 999):
        largest_b = c - 1
        for b in xrange(1, largest_b+1):
            largest_c = b - 1
            for a in xrange(0, largest_c+1):
                if a + b + c == 1000:
                    if (a**2)+(b**2) == (c**2):
                        return a*b*c
    return -1


if __name__ == '__main__':
    print problem9()

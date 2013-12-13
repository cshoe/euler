def is_prime(number):
    """
    Check if `number` is prime. `number` is assumed to be an integer.
    """
    if number == 2:
        return True

    if number <= 1 or number % 2 == 0:
        return False

    # check to see if number has any odd factors
    for x in range(3, int(number ** 0.5) + 1, 2):
        if number % x == 0:
            return False
    return True


def fib():
    """
    Generator to get fib seq.
    """
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y

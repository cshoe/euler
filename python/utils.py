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

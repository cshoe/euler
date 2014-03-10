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


def triangle_numbers():
    """
    Generate triangle numbers.

    The sequence of triangle numbers is generated by adding the natural
    numbers. So the 7th triangle number would be
    1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
    """
    counter, tri_number = 1, 1
    while True:
        yield tri_number
        counter += 1
        tri_number += counter


def divisor_lister(num):
    """
    Return a list of numbers that evenly divide into ``num``. Only works on
    positive, non-zero numbers.
    """
    if num <= 0:
        raise ValueError('num must be a positive, non-zero number')

    divisors = []
    for possible_divisor in range(2, num-1):
        if num % possible_divisor == 0:
            divisors.append(possible_divisor)

    # 1 and num itself are divisors so throw them in there
    divisors.append(1)
    divisors.append(num)
    divisors.sort()
    return divisors


def divisor_counter(num):
    """
    Return a count of divisors for num.  Only works on positive, non-zero
    numbers.
    """
    if num <= 0:
        raise ValueError('num must be a positive, non-zero number')

    divisors = 0
    for possible_divisor in range(1, int(num**.5)):
        if num % possible_divisor == 0:
            divisors += 1

    return divisors*2

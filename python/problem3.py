def problem3():
    """
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?

    """
    n = 600851475143
    largest = -1
    # brute force
    for x in range(int(n ** 0.5), n):
        if n % x == 0 and is_prime(x):
            largest = x

    print largest


def is_prime(number):
    """
    Check if `number` is prime.

    :param number assumed to be an integer.

    """
    if number == 2:
        return True

    if number <= 1 or number % 2 == 0:
        return False

    for x in range(3, int(number ** 0.5) + 1, 2):
        if number % x == 0:
            return False
    return True


if __name__ == '__main__':
    problem3()

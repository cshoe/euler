from utils import is_prime


def problem10():
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all primes below two million.
    """
    total_sum = 0
    for x in xrange(1, 2000000):
        if is_prime(x):
            total_sum += x
    return total_sum
    

if __name__ == '__main__':
    print problem10()

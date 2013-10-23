from utils import is_prime


def problem3():
    """
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143?
    """
    n = 600851475143
    largest = -1
    # brute force
    for x in range(1, int(n ** 0.5)):
        if n % x == 0 and is_prime(x):
            print 'largest is now {0}'.format(x)
            largest = x

    print largest

if __name__ == '__main__':
    problem3()

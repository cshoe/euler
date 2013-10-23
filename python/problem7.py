from utils import is_prime


def problem7():
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see
    that the 6th prime is 13.

    What is the 10 001st prime?
    """
    prime_count = 0
    current_try = 0
    # unbounded loops make me sad
    while True:
        if is_prime(current_try):
            prime_count += 1
            if prime_count == 10001:
                break
        current_try += 1

    print current_try


if __name__ == '__main__':
    problem7()

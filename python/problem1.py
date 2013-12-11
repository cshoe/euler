def problem1():
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    multiples = []
    total_sum = 0
    x = 3
    while x < 1000:
        if x % 3 == 0 or x % 5 == 0:
            total_sum += x
        x+=1;

    print total_sum

if __name__ == '__main__':
    problem1()

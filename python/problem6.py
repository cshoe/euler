def problem6():
    """
    The sum of the squares of the first tne natural numbers is 385.

    The square of the sum of the first ten naturral numbers is 3025.

    Hence the difference between the sum of the squares of the first
    tne natural numbers and the square of the sum is 3025 - 385 = 2640.

    Find hte difference of the sum of the squares of the first one hundred
    natural numbers and the square of the sum.

    """
    sum_of_sqs = sum_of_squares(100)
    sq_of_sum = square_of_the_sum(100)

    print sq_of_sum - sum_of_sqs


def sum_of_squares(length):
    """
    Find the sum of squares for the first `length` natural nunmbers.
    """
    return sum([x**2 for x in xrange(1, length+1)])


def square_of_the_sum(length):
    """
    Find the square of the sum of the first `length` natural numbers.
    """
    return sum([x for x in xrange(1, length+1)])**2

if __name__ == '__main__':
    problem6()

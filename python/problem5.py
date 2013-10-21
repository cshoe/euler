def problem5():
    """
    2520 is the smallest number that can be divided by each of the numbers from
    1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all the
    numbers from 1 to 20?
    """
    possible_answer = 20
    found = False
    while not found:
        for x in xrange(1, 21):
            if possible_answer % x != 0:
                possible_answer += 1
                break
        # else statement is only triggered if a the break statement above was
        # never hit
        else:
            found = True

    print possible_answer

if __name__ == '__main__':
    problem5()

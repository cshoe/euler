def problem4():
    """
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 x 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    largest_palindrome = 0
    for x in range(100, 1000):
        for y in range(100, 1000):
            product = x * y
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product

    print largest_palindrome


def is_palindrome(number):
    """
    Check if `number` is a palindrome.

    `number` is assumged to be an integer.
    """
    num_str = str(number)
    first_half = num_str[:len(num_str)/2]
    rev_second_half = num_str[len(num_str)/2:][::-1]
    return first_half == rev_second_half


if __name__ == '__main__':
    problem4()

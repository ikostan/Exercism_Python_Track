def largest(min_factor, max_factor):
    """
    Returns the largest palindrome product and its factors

    :param min_factor:
    :param max_factor:
    :return:
    """

    return main_func(min_factor, max_factor, False)


def smallest(min_factor, max_factor):
    """
    Returns the smallest palindrome product and its factors

    :param min_factor:
    :param max_factor:
    :return:
    """

    return main_func(min_factor, max_factor, True)


def main_func(min_factor, max_factor, is_smallest):

    products = get_products(min_factor, max_factor, is_smallest)

    if not products:
        return None, []

    # This flag indicates if we looking for smallest/largest palindrome
    if is_smallest:
        palindrome = min(products.keys())
    else:
        palindrome = max(products.keys())

    factors = products[palindrome]

    print('{} : {}'.format(palindrome, factors))
    return palindrome, factors


def get_products(min_factor, max_factor, is_smallest):
    """
    Generate a dictionaries where:
        KEY - palindrome
        VALUES - products that creates KEY

    In order to optimize the solution is_smallest flag implemented.
    This flag indicates if we looking for smallest/largest palindrome

    :param min_factor:
    :param max_factor:
    :param is_smallest:
    :return:
    """

    # Raise an error in case min > max
    if min_factor > max_factor:
        raise ValueError(".+")

    # Return None in case min == max
    if min_factor == max_factor:
        return None

    nums = dict()

    if is_smallest:
        min_f = min_factor

        while min_factor <= max_factor:
            m = min_f
            while m <= max_factor:
                n = min_factor * m

                # break the loop since all next numbers will be bigger
                if len(nums.keys()) != 0 and n > min(nums.keys()):
                    break

                # Test if a result is palindrome
                if is_palindrome(n):

                    if not nums:
                        nums[n] = [[min_factor, m]]
                    else:
                        if n < min(nums.keys()):
                            nums[n] = [[min_factor, m]]
                        elif n == min(nums.keys()):
                            if [min_factor, m] not in nums[n]:
                                nums[n].append([min_factor, m])
                        else:
                            break

                m += 1
            min_factor += 1

    if not is_smallest:
        max_f = max_factor

        while max_factor >= min_factor:
            m = max_f
            while m >= min_factor:
                n = max_factor * m

                # break the loop since all next numbers will be smaller
                if len(nums.keys()) != 0 and n < max(nums.keys()):
                    break

                # Test if a result is palindrome
                if is_palindrome(n):

                    if not nums:
                        nums[n] = [[max_factor, m]]
                    else:
                        if n > max(nums.keys()):
                            nums[n] = [[max_factor, m]]
                        elif n == max(nums.keys()):
                            if [max_factor, m] not in nums[n]:
                                nums[n].append([max_factor, m])
                        else:
                            break

                m -= 1
            max_factor -= 1

    return nums


def is_palindrome(number):
    '''
    Reverse string and compare to itself.
    Returns True uin case number is palindrome, false otherwise.
    :param number:
    :return:
    '''

    return str(number) == str(number)[::-1]


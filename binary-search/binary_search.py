def find(search_list: list, value: int) -> int:
    """
    Implement a binary search algorithm.

    :param search_list: a sorted list of values
    :param value: value to search
    :return: index of value in the search_list
    """

    # Raise error in case list is empty
    if not search_list:
        raise ValueError("ERROR: the search list is empty!")

    left, right, mid = 0, len(search_list) // 2, len(search_list) - 1
    # In each step, the algorithm compares the search key value with
    # the key value of the middle element of the array.
    while left <= right:

        # if the search key is greater, on the sub-array to the right
        if value > search_list[mid]:
            left = mid + 1
            mid = (mid + right) // 2

        # if the search key is less than the middle element's key,
        # then the algorithm repeats its action on the sub-array
        # to the left of the middle element
        if value < search_list[mid]:
            right = mid - 1
            mid = mid // 2

        # If the keys match, then a matching element has been
        # found and its index, or position, is returned.
        if value == search_list[mid]:
            return mid

    # Value is not in search list
    raise ValueError("ERROR: {} not in search list!".format(value))

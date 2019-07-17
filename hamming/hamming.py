def distance(strand_a, strand_b):
    '''
    Calculate the Hamming Distance between two DNA strands.
    :param strand_a:
    :param strand_b:
    :return:
    '''

    # Return error if DNA strands have different length:
    if len(strand_a) != len(strand_b):
        raise ValueError('.+')

    # Calculate Hamming Distance:
    hamming_distance = 0
    for i, s in enumerate(strand_a):
        if s != strand_b[i]:
            hamming_distance += 1

    return hamming_distance


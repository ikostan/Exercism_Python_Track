def distance(strand_a, strand_b):
    '''
    Calculate the Hamming Distance between two DNA strands.
    :param strand_a:
    :param strand_b:
    :return:
    '''

    # Return error if DNA strands have different length:
    if len(strand_a) != len(strand_b):
        raise ValueError('ERROR: DNA strands have different length.')

    # Calculate Hamming Distance and return it:
    return sum([1 for z in zip(strand_a, strand_b) if z[0] != z[1]])





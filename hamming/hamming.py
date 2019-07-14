def distance(strand_a, strand_b):

    if len(strand_a) != len(strand_b):
        raise ValueError('.+')

    hamming_distance = 0
    for i, s in enumerate(strand_a):
        if s != strand_b[i]:
            hamming_distance += 1

    return hamming_distance


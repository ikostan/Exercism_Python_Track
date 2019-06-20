def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    '''
    Old solution:

    if len(scores) >= 3:
        start = len(scores) - 3
        return sorted(sorted(scores)[start:], reverse=True)
    else:
        return sorted(scores, reverse=True)

    :param scores:
    :return:
    '''

    return sorted(scores, reverse=True)[:3]


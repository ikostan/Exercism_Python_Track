def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    if len(scores) >= 3:
        start = len(scores) - 3
        return sorted(sorted(scores)[start:], reverse=True)
    else:
        return sorted(scores, reverse=True)
